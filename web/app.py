import json
import requests
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, StringField, PasswordField, validators, ValidationError
from pymongo import MongoClient

# 以下にコードを記入

app = Flask(__name__)
# ローカルのMongoDBに接続
client = MongoClient()
# jdmcawsデータベースを作成
db = client['jdmcaws']
# ordersテーブルを作成
coll = db['orders']

# レシピUUID：固定
RECIPIE_UUID = 'your recipie UUID'
EVS_ROOT_URL = 'https://api.every-sense.com:8001/get_output_data'

# フォームデータを保持するクラス
class OrderForm(Form):
    input_login_name = StringField(u'ログイン名', [validators.Required()])
    input_login_pass = PasswordField(u'パスワード', [
        validators.Required()
    ])

@app.route('/')
def root():
    form = OrderForm(request.form)
    return render_template('index.html', form=form)

# エブリセンスのAPIへPOSTリクエスト
@app.route('/post', methods=['POST'])
def post():
    form = OrderForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['input_login_name']
        password = request.form['input_login_pass']
        # エブリセンスのAPIを叩いて、データを取得
        response = make_EVS_request(
            {"login_name" : name, "password" : password}
        )
        # レスポンスから、JSONデータを解析
        output = retrieve_json_date(response)
        return render_template('result.html', form=form, name=name, output=output)
    else:
        return render_template('index.html')

def make_EVS_request(params=None,recipie_UUID=RECIPIE_UUID,root_dir=EVS_ROOT_URL):

    if params is None:
        params = {}
    # POSTリクエスト作成
    params['recipe_uuid'] = recipie_UUID
    params['keep'] = 'true'
    params['limit'] = 10
    params['format'] = 'JSON'
    params['from'] = '2017-12-01 12:00:01 UTC'
    params['to'] = '2017-12-08 12:10:00 UTC'
    json_param = json.dumps(params).encode('utf-8')
    every_response = requests.post(root_dir, data=json_param,headers={'Content-Type': 'application/json'})
    return every_response

def retrieve_json_date(response):
    # レスポンスからデータ抜き出し
    everypost_orders = response.json()
    parent_count = len(everypost_orders)
    out_dict = []
    for m in range(0,parent_count):
        child_count = len(everypost_orders[m])
        for n in range(0,child_count):
            if everypost_orders[m][n]['data_class_name'] == 'Location':
                out_dict.append([everypost_orders[m][n]['data']])
    return(out_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
