import logging
from logging.handlers import RotatingFileHandler
import os
import random
import string

def start_up(app, app_config):
    # set log file
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s: %(message)s "
        "[in %(pathname)s:%(lineno)d]"
    )

    # for debug log
    debug_log = app_config.debug_path
    debug_file_handler = RotatingFileHandler(
        debug_log, maxBytes=100000, backupCount=10
    )
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)
    app.logger.addHandler(debug_file_handler)
    
    # for error log

    error_log = app_config.error_path
    error_file_handler = RotatingFileHandler(
        error_log, maxBytes=100000, backupCount=10
    )
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)
    
    line = ""
    current_dir = os.path.dirname(__file__)
    f_name = os.path.join(current_dir, "data/secretkey")
    if not os.path.exists(f_name):
        with open(f_name, "w") as f:
            l = [random.choice(string.ascii_letters + string.digits) for i in range(100)]
            f.write("".join(l))
    with open(f_name, "r") as f:
        line = f.readline().strip()
    SECRET_KEY = line
    app.config['SECRET_KEY'] = SECRET_KEY
