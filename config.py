import os
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from qa_guru_python_22.utils.file import abs_path_from_project


class Config:
    app = os.getenv('APP')
    remote_url = os.getenv('REMOTE_URL')
    device_name = os.getenv('DEVICE_NAME')
    udid = os.getenv('UDID')
    app_wait_activity = os.getenv('APP_WAIT_ACTIVITY')
    platform_name = os.getenv("PLATFORM_NAME")
    platform_version = os.getenv("PLATFORM_VERSION")
    load_dotenv('.env.credentials')
    user_Name = os.getenv('USER_NAME')
    access_key = os.getenv('ACCESS_KEY')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platform_name)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability('app', self.app)
            options.set_capability(
                'bstack:options',
                {
                    'projectName': 'Wikipedia tests project',
                    'buildName': 'Wikipedia-app-build',
                    'sessionName': 'Wikipedia tests',
                    'userName': self.user_Name,
                    'accessKey': self.access_key,
                },
            )
        if context == 'local_emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('app', abs_path_from_project(self.app))

        if context == 'local_real_device':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('udid', self.udid)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('app', abs_path_from_project(self.app))

        return options


config_app = Config()
