import os

SESSION_ID = os.getenv('SESSION_ID')
if SESSION_ID is None:
    SESSION_ID = '8okfl9z8yftehjw8btj3codtbuy46db1'

BASE_URL =  os.getenv('BASE_URL')
if BASE_URL is None:
    BASE_URL = 'http://localhost:8000/'
