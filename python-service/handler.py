import json
from jinja2 import Environment, FileSystemLoader
from cerberus import Validator
import urllib
import base64

schema = {
    'name': {
        'required': True,
        'type': 'list',
        'schema': {
            'type': 'string'
        }
    }
}

def hello(event, context):
    env = Environment(loader=FileSystemLoader('./templates', encoding='utf8'))
    template = env.get_template('index.html')
    html = template.render()
    print(json.dumps(event))
    print(type(event['body']))
    print(json.dumps(base64.b64decode(event['body']).decode()))
    post_params = urllib.parse.parse_qs(base64.b64decode(event['body']).decode())
    print(json.dumps(post_params))
    show_validate(post_params, schema)
    response = {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html
    }

    return response


def show_validate(data, schema):
    v = Validator(schema)
    print(data)
    print(v.validate(data))
    print(v.errors)

