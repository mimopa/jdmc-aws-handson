import boto3
 
BUCKET_NAME = 'mscexample00'
TARGET_DIR = "abc"
PUT_FILENAME = "dataset.csv"

# 高レベルAPIのみを使用してS3バケットにCSVファイルを保存する
# put()メソッドの引数Bodyに保存したい内容をバイト列として渡す。
def lambda_handler(event, context):
    
    # S3
    s3 = boto3.resource('s3')
    
    # バケットを取得
    bucket = s3.Bucket(BUCKET_NAME)
    
    # ファイル内容
    FILE_CONTENTS = u'ファイルコンテンツ'
    
    # ファイル出力
    ret = bucket.put_object( \
        ACL='private', \
        Body=FILE_CONTENTS, \
        Key=TARGET_DIR + "/" + FILENAME, \
        ContentType='text/plain' \
    )
     
    return str(ret)