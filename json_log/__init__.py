name = 'json_log'
from distutils.util import strtobool
from dotenv import load_dotenv
load_dotenv()
import yaml

config = yaml.safe_load(open('config.yml'))

use_fluentd = strtobool(str(config['LOG_FLUENTD']))

if use_fluentd:
    from .fluentd_log import applog
else:
    from .file_log import applog

applog = applog