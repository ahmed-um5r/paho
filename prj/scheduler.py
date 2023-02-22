from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2
from django.conf import settings
from django.db import connection 

def my_task():
    
    conn = psycopg2.connect(
        host="localhost",
        database="test",
        user="postgres",
        password="postgres"
    )
    cursor = conn.cursor()
    
    cursor.execute("insert into test0_country(name, number_of_club)  VALUES ( 'nn',3)") 
    conn.commit()
    cursor.close()
    conn.close()

#    print("Hello, world!")

scheduler = BackgroundScheduler()
scheduler.add_job(my_task, 'interval', seconds=10)
scheduler.start()