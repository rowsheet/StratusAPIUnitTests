import os

SESSION_ID = os.getenv('SESSION_ID')
if SESSION_ID is None:
    SESSION_ID = 'b4wn10ra58g8ehdqkc0n4t0cx1e7nt5q'

BASE_URL =  os.getenv('BASE_URL')
if BASE_URL is None:
    BASE_URL = 'https://rowsheet-stratus-rebuild.herokuapp.com/'
