FROM public.ecr.aws/lambda/python:3.9

COPY python-service/ ${LAMBDA_TASK_ROOT}
RUN  yum install -y postgresql-libs && pip install --upgrade pip && pip install -r requirements.txt
CMD ["app.handler"]
