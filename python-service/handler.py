import json
from jinja2 import Environment, FileSystemLoader
from cerberus import Validator
import urllib
import base64

from schema.user import user
from schema.item import item

def hello(event, context):
    print(json.dumps(event))
    print(type(event['body']))
    # GETの入力チェック
    if event['httpMethod'] == "GET":
        #get_params=urllib.parse.parse_qs(event['queryStringParameters'])
        for k, v in event['queryStringParameters'].items():
            print(type(k))
            print(k)
            print(type(v))
            print(v)
        show_validate(event['queryStringParameters'], item)
    # POSTの入力チェック
    elif event['httpMethod'] == "POST":
        post_params = urllib.parse.parse_qs(base64.b64decode(event['body']).decode())
        print(post_params["age"])
        show_validate(post_params, user)

    # HTMLテンプレート
    env = Environment(loader=FileSystemLoader('./templates', encoding='utf8'))
    template = env.get_template('index.html')
    html = template.render()
    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html
    }

    return response


def show_validate(data, schema):
    v = Validator(schema)
    print(v.validate(data))
    print(v.errors)

