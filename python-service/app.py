import json
import urllib
import base64
import psycopg2
import sys
from jinja2 import Environment, FileSystemLoader
from cerberus import Validator

from schema.user import user
from schema.item import item

class Database():
    """Database
    """
    class Parameter():
        """Parameter
        """

        def __init__(self, host, port, dbname, table, user, password, query):
            self.host = host
            self.port = port
            self.dbname = dbname
            self.table = table
            self.user = user
            self.password = password
            self.query = query

    def __init__(self, param):
        self.db = param
        self.header = tuple()
        self.records = list()
        self.counts = int()

    def _connection(self):
        """_connection
        """
        print('connect to db: {}/{}'.format(self.db.host, self.db.dbname))
        return psycopg2.connect(
            host=self.db.host,
            port=self.db.port,
            dbname=self.db.dbname,
            user=self.db.user,
            password=self.db.password
        )

    def query(self):
        """query
        """
        with self._connection() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(self.db.query)
                    self.header = cursor.description
                    self.records = cursor.fetchall()
                    self.counts = len(self.records)
                except psycopg2.Error as e:
                    print(e)
                    sys.exit()
        return True

def handler(event, context):
    print(json.dumps(event))
    print(type(event['body']))
    
    param = Database.Parameter(
        host='xxxx',
        port='xxxx',
        dbname='xxxx',
        table='xxxx',
        user='xxxx',
        password='xxxx',
        query='xxxx'
    )
    db = Database(param=param)
    db.query()

    print(str(db.records))
    print(db.counts)

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
