import logging
import json
from uuid import uuid4
from .utils.data_format import sanitize_json
from .generic_log import GenericLog


class AppLog(GenericLog):

    def __init__(self, log_name):

        app_log = logging.getLogger(log_name)
        app_log.setLevel(logging.getLevelName(self.log_level))

        ch = logging.FileHandler(f'./log/{log_name}.log')
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
                nodes_list.append(f'\"{key}\" : \"{sanitize_json(value)}\"')

        formated_message = ','.join(nodes_list)

        return formated_message

applog = AppLog('processa_pedidos')
