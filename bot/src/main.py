import os
import logging
from datetime import datetime
from bot import Bot


if __name__ == '__main__':
    _now = datetime.now()
    _log_name = _now.strftime('%m-%d-%Y-%H-%M-%S')
    _log_file = f'../log/{_log_name}.log'
    
    logging.basicConfig(
        filename=_log_file,
        filemode='w',
        format='%(asctime)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        level=logging.INFO
    )

    bot = Bot(
        os.getenv('ADDRESS'),
        os.getenv('PRIVATE_KEY')
    )

    bot.run()

    
