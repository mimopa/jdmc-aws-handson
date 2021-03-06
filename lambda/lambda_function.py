import json
import requests
import boto3
import urllib
import time
import decimal

from datetime import datetime, timedelta, timezone
from dateutil import parser

# DynamoDBオブジェクト
dynamodb = boto3.resource('dynamodb')
# エブリセンスのデータ出力APIエンドポイント
EVS_ROOT_URL = 'https://api.every-sense.com:8001/get_output_data'
# 連番を更新して返す関数
def next_seq(table, tablename):
    response = table.update_item(
        Key={
            'tablename' : tablename
        },
        UpdateExpression="set seq = seq + :val",
        ExpressionAttributeValues= {
            ':val' : 1
        },
        ReturnValues='UPDATED_NEW'
    )
    return response['Attributes']['seq']

# Lambda関数呼び出し時に最初に呼ばれる関数
def everypost_handler(event, context):
    try:
        # DynamoDBのテーブルインスタンス作成(sequenceテーブル)
        seqtable = dynamodb.Table('sequence')
        
        # フォームに入力されたデータを得る
        param = urllib.parse.parse_qs(event['body'])
        #print(event['body'])
        # paramが取得取得できなかった場合、JSONとして処理処理しないとだめ？
        # AJAXでPOST（JSON形式）した場合（True）と、HTMLのWebフォームからPOSTした場合（False）で取得方法が異なる
        if param == "" and isinstance(event['body'], str):
            body = json.loads(event['body'])
            recipe_uuid = body['recipe_uuid']
            session_key = body['session_key']
        else:
            recipe_uuid = param['recipe_uuid']
            session_key = param['session_key']
        
        # エブリセンス社のデータ出力APIを叩いて、データを取得
        response = make_EVS_request(
            {"session_key" : session_key, "recipe_uuid" : recipe_uuid}
        )
        # レスポンスから、JSONデータを解析
        output = retrieve_json_data(response)
        
        # DynamoDBのテーブルインスタンス作成(sensordataテーブル)
        sensortable = dynamodb.Table("sensordata")
        
        # outputに格納されているList分、繰り返して登録する（batch_writer()を利用）
        with sensortable.batch_writer() as batch:
            for outItem in output:
                # atの処理（文字列UTC→文字列JST）
                jst_time = parser.parse(outItem[0]['at']).astimezone(timezone(timedelta(hours=+9), 'JST'))
                jst_time_str = datetime.strftime(jst_time, '%Y-%m-%d %H:%M:%S')
                
                batch.put_item(
                    Item={
                        'id' : next_seq(seqtable, 'sensordata'),
                        'farm_uuid' : outItem[0]['farm_uuid'],
                        'at' : jst_time_str,
                        'latitude' : decimal.Decimal(str(outItem[0]['location']['latitude'])),
                        'longitude' : decimal.Decimal(str(outItem[0]['location']['longitude']))
                    }
                )
        
        # 結果を返す
        return {
            'statusCode' : 200,
            'headers' : {
                'content-type' : 'text/html'
            },
            'body' : '<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body>データ取得が完了しました。次は可視化してみましょう！</br><a href="http://jdmchandson001.s3-website-ap-northeast-1.amazonaws.com/">戻る </a></body></html>'
        }
    except:
        import traceback
        traceback.print_exc()
        return {
            'statusCode' : 500,
            'headers' : {
                'content-type' : 'text/html'
            },
            'body' : '<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body>内部エラーが発生しました。</body></html>'
        }

def make_EVS_request(params=None,root_dir=EVS_ROOT_URL):

    if params is None:
        params = {}
    # POSTリクエスト作成（固定部分）
    params['keep'] = 'true'
    params['limit'] = 500
    params['format'] = 'JSON'
    params['from'] = '2017-12-28 15:00:00 UTC'
    params['to'] = '2018-03-31 23:10:00 UTC'
    json_param = json.dumps(params).encode('utf-8')
    every_response = requests.post(root_dir, data=json_param,headers={'Content-Type': 'application/json'})
    return every_response

def retrieve_json_data(response):
    # レスポンスからデータ抜き出し
    # ToDo：ファームUUIDの取得により、可視化時に自分（特定）のデータを選択可能とする
    everypost_orders = response.json()
    parent_count = len(everypost_orders)
    out_list = []
    for m in range(0,parent_count):
        child_count = len(everypost_orders[m])
        for n in range(0,child_count):
            out_dict = {}
            if everypost_orders[m][n]['data_class_name'] == 'Location':
                out_dict = everypost_orders[m][n]['data']
                out_dict['farm_uuid'] = everypost_orders[m][n]['farm_uuid']
                out_list.append([out_dict])
    return(out_list)
