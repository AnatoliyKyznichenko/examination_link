from dotenv import dotenv_values
from services.api_sqlite import *

config_file = dotenv_values('.env')
# db = UserLink()