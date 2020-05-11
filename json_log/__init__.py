name = 'json_log'
from os import environ
from distutils.util import strtobool
from dotenv import load_dotenv
load_dotenv()

local_log_env = strtobool(str(environ.get('LOCAL_LOG', 'True')))
force_local_env = strtobool(str(environ.get('FORCE_LOCAL_LOG', 'False')))

if local_log_env or force_local_env:
    from .file_log import applog
else:
    from .fluentd_log import applog

applog = applog