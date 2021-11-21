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
        get_params = event['queryStringParameters']
        param = {
            'name': get_params.get('name'),
            'age': get_integer(get_params.get('age'))
        }
        show_validate(param, item)
    # POSTの入力チェック
    elif event['httpMethod'] == "POST":
        post_params = urllib.parse.parse_qs(base64.b64decode(event['body']).decode())
        param = {
            'name': post_params.get('name')[0],
            'age': get_integer(post_params.get('age')[0])
        }
        print(json.dumps(param))
        show_validate(param, user)

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

def get_integer(str):
    try:
        return int(str)
    except Exception:
        return str

def get_float(str):
    try:
        return float(str)
    except Exception:
        return str
