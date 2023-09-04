from apscheduler.schedulers.background import BackgroundScheduler
from rocketry import Rocketry
from rocketry.conds import (
    every, hourly, daily,
    after_success,
    true, false
)
from ..servidores import Twillo
from datetime import datetime
from ..packages.connection import db


def enviar_mensagens():
    try:
        cursor = db.cursor()
        cursor.execute(f'''SELECT * FROM sms WHERE data = {str(datetime.now())[:10]}''')
        mensagens = cursor.fetchall()
    except:
        pass


scheduler = BackgroundScheduler()
scheduler.add_job(enviar_mensagens, 'interval', seconds=10)


if __name__ == '__main__':
    scheduler.start()
