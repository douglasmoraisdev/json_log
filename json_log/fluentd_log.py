import json
import logging
from uuid import uuid4
from fluent import handler
from os import environ
from .generic_log import GenericLog

from dotenv import load_dotenv
load_dotenv()

from .utils.data_format import sanitize_json


class FluentdLog(GenericLog):

    def __init__(self, log_name):
        fluentd_log = logging.getLogger(log_name)
        fluentd_log.setLevel(logging.getLevelName(self.log_level))

        ch = handler.FluentHandler(
            log_name,
            host=environ.get('FLUENTD_HOST', 'localhost'),
            port=int(environ.get('FLUENTD_PORT', 24224))
        )
        ch.setLevel(logging.getLevelName(self.log_level))
        custom_format = {
            "appname": "%(name)s",
            "loglevel": "%(levelname)s",
            "run_id": "%(run_id)s",
        }

        formatter = handler.FluentRecordFormatter(custom_format)
        ch.setFormatter(formatter)
        fluentd_log.addHandler(ch)

        self.log = fluentd_log
        self.run_id = uuid4()

    '''
    def info(self, message, **kwargs):
        msg = {'message': message}
        kwargs.update(msg)
        message = kwargs
        self.log.info(message, extra={'run_id': self.run_id})

    def error(self, message, **kwargs):
        msg = {'message': message}
        kwargs.update(msg)
        message = kwargs
        self.log.error(message, extra={'run_id': self.run_id})

    def debug(self, message, **kwargs):
        msg = {'message': message}
        kwargs.update(msg)
        message = kwargs
        self.log.debug(message, extra={'run_id': self.run_id})
    '''


applog = FluentdLog('pedidos_online')
