from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2

from django.conf import settings
from django.db import connection
import MySQLdb

#def hi():


def print_message():
    print("Hello, world!")

#scheduler = BackgroundScheduler()
#scheduler.add_jobstore(DjangoJobStore(), "default")
#scheduler.add_job(print_message, "interval", seconds=15)
#scheduler.start()