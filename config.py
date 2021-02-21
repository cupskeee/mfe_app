# App Settings
APP_HOST = "0.0.0.0"
APP_PORT = 5000
APP_DEBUG = True
# This Secret key is a Base64 form of 'rspi-am'
SECRET_KEY = 'cnNwaS1hbQ=='

# Flask-User settings
USER_APP_NAME = "Dev RSPI Assets Management"  # Shown in and email templates and page footers
USER_ENABLE_EMAIL = False  # Disable email authentication
USER_ENABLE_USERNAME = True  # Enable username authentication
USER_REQUIRE_RETYPE_PASSWORD = False  # Simplify register form

# SQLAlchemy Settings
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1:3306/rspi-am-dev'
# SQLALCHEMY_DATABASE_URI = 'mysql://macb8717:83ZMAFpyNbVT15@127.0.0.1:3306/rspi-am'
SQLALCHEMY_TRACK_MODIFICATIONS = False
