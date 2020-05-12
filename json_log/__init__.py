name = 'json_log'
from os import environ
from distutils.util import strtobool
from dotenv import load_dotenv
load_dotenv()

use_fluentd = strtobool(str(environ.get('LOG_FLUENTD', 'False')))

if use_fluentd:
    from .fluentd_log import applog
else:
    from .file_log import applog

applog = applog