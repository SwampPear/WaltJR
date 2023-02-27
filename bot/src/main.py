import os
import logging
from bot import Bot


if __name__ == '__main__':
    logging.basicConfig(
        filename='../log/bot.log',
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

    
