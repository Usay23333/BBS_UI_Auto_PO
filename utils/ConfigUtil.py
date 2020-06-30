# coding=utf-8

from configparser import ConfigParser
import os

class ConfigReader():
    __instance = None # 这个类的实例

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.cf = ConfigParser()
        self.config_path = os.path.join(os.path.abspath(__file__), '..\..', 'config', 'config.ini')
        self.cf.read(self.config_path, encoding='utf-8')

    def get_bbs(self, option):
        return self.cf.get('bbs', option)

    def get_email(self, option):
        return self.cf.get('email', option)

    def get_db(self, option):
        return self.cf.get('database', option)

    def get_project(self, option):
        return self.cf.get('project', option)

    def get_log(self, option):
        return self.cf.get('log', option)

if __name__ == "__main__":
    print(ConfigReader().get_email("server_host"))
