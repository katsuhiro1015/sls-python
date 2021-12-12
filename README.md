# sls-python

## setup
### create 

```
$ serverless create --template aws-python3 --name python-service --path python-service
```

## deploy

```
$ cd python-service
$ sls deploy
```

## バリデート


### GETリクエストの取得

### POSTリクエストの取得

### 必須チェック

```
$ cd python-service
$ pip3 install -t . cerberus
```

### 文字種チェック

### 文字列長チェック


## HTMLテンプレート

### jinja2

```
$ cd python-service
$ pip3 install -t . jinja2
```

postgreSQL

CREATE TABLE demo (id char(4) not null, PRIMARY KEY(id));
insert into demo values('1');

aws ecr get-login-password | docker login --username AWS --password-stdin 165985788939.dkr.ecr.ap-northeast-1.amazonaws.com