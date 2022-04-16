from datetime import datetime, timedelta

def sleep(time):
    sleepTime = timedelta(seconds = time)
    start_time = datetime.now()       
    while start_time + sleepTime > datetime.now():
        pass
