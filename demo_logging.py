# coding=utf-8

import logging, os
from time import strftime
from utils.ConfigUtil import ConfigReader

project_path = ConfigReader().get_project('path')
log_name = strftime("%Y-%m-%d") + '.log'
log_path = os.path.join(project_path, 'log', log_name)

logging.basicConfig(filename=log_path,level=logging.DEBUG)

logging.debug(f'log_debug --- {strftime("%Y-%m-%d %H-%M-%S")}')
logging.info(f'log_info --- {strftime("%Y-%m-%d %H-%M-%S")}')
logging.warning(f'log_warning --- {strftime("%Y-%m-%d %H-%M-%S")}')
logging.error(f'log_error --- {strftime("%Y-%m-%d %H-%M-%S")}')
logging.critical(f'log_critical --- {strftime("%Y-%m-%d %H-%M-%S")}')