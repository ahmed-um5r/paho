from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2

from django.conf import settings
from django.db import connection

#def hi():


def hi():
    print('test')