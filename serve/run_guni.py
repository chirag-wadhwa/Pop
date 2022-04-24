'''
Chirag Wadhwa 2019A7PS0103P
V Sushant 2019A7PS0045P
'''

import os
from api import app

if __name__ == "__main__":
    app.run()

# To Run:
# yarn build
# gunicorn -w 8 run_guni:app -b 127.0.0.1:5000
