import json
import logging
from uuid import uuid4
from fluent import handler
from os import environ
from .generic_log import GenericLog

from dotenv import load_dotenv
load_dotenv()


class FluentdLog(GenericLog):

    def __init__(self, log_name):
        fluentd_log = logging.getLogger(log_name)
        fluentd_log.setLevel(logging.getLevelName(self.log_level))

        ch = handler.FluentHandler(
            log_name,
            host=environ.get('LOG_FLUENTD_HOST', 'localhost'),
            port=int(environ.get('LOG_FLUENTD_PORT', 24224))
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

log_level = environ.get('LOG_NAME', 'json_log')
applog = FluentdLog(log_level)
