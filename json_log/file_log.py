import logging
import json
from uuid import uuid4
from .generic_log import GenericLog
from pathlib import Path
import yaml

config = yaml.safe_load(open('config.yml'))

class AppLog(GenericLog):

    def __init__(self, log_name):

        app_log = logging.getLogger(log_name)
        app_log.setLevel(logging.getLevelName(self.log_level))

        path = Path(self.log_path)
        path.mkdir(parents=True, exist_ok=True)

        ch = logging.FileHandler(f'{self.log_path}{log_name}.log')
        ch.setLevel(logging.getLevelName(self.log_level))

        formatter = logging.Formatter('{'
                                      ' "@timestamp": "%(asctime)s",'
                                      ' "appname": "%(name)s",'
                                      ' "loglevel": "%(levelname)s",'
                                      ' "run_id": "%(run_id)s",'
                                      ' %(message)s'
                                      '}'
                                      )

        ch.setFormatter(formatter)
        app_log.addHandler(ch)

        self.log = app_log
        self.run_id = uuid4()

    def _format_message(self, **kwargs):
        nodes_list: list = []
        for key, value in kwargs.items():
            if type(value) is list:
                nodes_list.append(f'\"{key}\" : {json.dumps(value)}')
            elif (type(value) is float) or (type(value) is int):
                nodes_list.append(f'\"{key}\" : {value}')
            else:
                nodes_list.append(f'\"{key}\" : \"{self._sanitize_json(value)}\"')

        formated_message = ','.join(nodes_list)

        return formated_message

log_level = config['LOG_LEVEL']
log_name = config['LOG_NAME']
applog = AppLog(log_name)
