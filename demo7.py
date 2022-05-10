import logging

logging.basicConfig(filename="logs/test.log", filemode="w",
                    format="%(asctime)s:%(pathname)s:第%(lineno)d行:%(name)s:%(levelname)s:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.NOTSET)

a = 5
b = 1
try:
    c = a / b
    logging.info('This is an info message')
except Exception as e:
    # 下面三种方式三选一，推荐使用第一种
    # logging.exception("Exception occurred")
    # logging.error("Exception occurred", exc_info=True)
    # logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)
    logging.error(e)
