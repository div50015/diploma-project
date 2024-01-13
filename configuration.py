import os
from pydantic import BaseModel
from diploma_project.utils import helpers
from appium.options.android import UiAutomator2Options


class Settings(BaseModel):
    context: str
    login: str = os.getenv('User_Name')
    password: str = os.getenv('Access_Key')
    appWaitActivity: str = os.getenv('appWaitActivity')
    remote_url: str = os.getenv('remote_url')
    udid: str = os.getenv('udid')
    app: str = os.getenv('app')
    platformVersion: str = os.getenv('platformVersion')
    deviceName: str = os.getenv('deviceName')
    projectName: str = os.getenv('projectName')
    buildName: str = os.getenv('buildName')
    sessionName: str = os.getenv('sessionName')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local_emulator':
            options: str = {
                'app': helpers.abs_path_from_project(self.app),
                'remote_url': self.remote_url,
                'udid': self.udid,
            }

        if context == 'local_real':
            options: str = {
                'app': helpers.abs_path_from_project(self.app),
                'remote_url': self.remote_url,
                'udid': self.udid
            }

        if context == 'bstack':
            options: str = {
                'platformVersion': self.platformVersion,
                'deviceName': self.deviceName,
                'app': self.app,
                'bstack:options': {
                    'projectName': self.projectName,
                    'buildName': self.buildName,
                    'sessionName': self.sessionName,
                    'userName': self.login,
                    'accessKey': self.password,
                }
            }

        return options


settings = Settings(context='local_real')
