from src.app import io, app
from src.tasks import scheduler
from src.events import *
from src.controllers import *


if __name__ == '__main__':
    scheduler.start()
    io.run(
        app=app,
        host='0.0.0.0',
        port=2021,
        debug=True
    )
