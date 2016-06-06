#coding:utf-8
import threading
from celery import Celery

class EventHandle(object):
    def __init__(self, context):
        self.context = context
        self.app = Celery('proxy',
                broker=self.context.broker,
                backend=self.context.backend)
        self.app.conf.update(
                CELERY_TASK_RESULT_EXPIRES=3600,
                CELERY_RESULT_PERSISTENT=True,
                CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml'],
        )

    def send(self, event):
        self.app.send_task('receive_flow', args=(event,), exchange='surge', routing_key='reciver')
