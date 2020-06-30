import os
import time
import logging
from utils.ConfigUtil import ConfigReader

def make_dir(make_dir_path):

    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path

class Logger():
    __instance = None  # 这个类的实例

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        # 配置文件中读取日志等级
        self.log_level = ConfigReader().get_log('level').upper()
        # 日志输入格式
        self.logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
        # 配置文件中读取日志文件夹路径
        self.log_dir_name = ConfigReader().get_log("path")
        # 日志文件名称
        self.log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
        # 拼接项目路径和日志文件夹
        self.log_file_folder = os.path.join(ConfigReader().get_project("path"), self.log_dir_name)
        make_dir(self.log_file_folder)

        self.log_file_str = self.log_file_folder + os.sep + self.log_file_name

        self.__logger = logging.getLogger()

        try:
            self.__logger.setLevel(self.log_level)
        except Exception as e:
            print(f"log_level error, please check config!\n{e}")
            exit(0)

        if not self.__logger.handlers:
            self.file_handler = logging.FileHandler(self.log_file_str, encoding='UTF-8')
            self.file_handler.setLevel(self.log_level)
            self.file_handler.setFormatter(self.logging_format)
            self.output_hanler = logging.StreamHandler()
            self.output_hanler.setLevel(self.log_level)
            self.output_hanler.setFormatter(self.logging_format)
            self.__logger.addHandler(self.file_handler)
            self.__logger.addHandler(self.output_hanler)

        logging.getLogger("selenium").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
    def instance(self):
        return self.__logger

if __name__ == "__main__":

    Logger().instance().debug("test debug")
    Logger().instance().info("test info")
    Logger().instance().error("test error")


