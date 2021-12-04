# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:00:00 2021

@author: Cedric Yu
"""

# import matplotlib.pyplot as plt
# import math
# import re


"""
# Flask

Exercise: Hello World

##############################

# 

##############################

# Summary: 

    # 

"""

#%% Hello World

from flask import Flask

# Flask class
app = Flask(__name__)

# the route() decorator tells Flask what URL should trigger our function
@app.route("/")
def hello_world():
    return "Hello, World!"


"""
To run, go to anaconda cmd, go to the directory of this file, and execute
(with FLASK_ENV = "development", webpage updates without having to restart server)

$env:FLASK_APP="1_hello_world.py"
$env:FLASK_ENV = "development"   
flask run

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
alias:
locahost:5000/


Alternatively, to start server by running this script, use

# if __name__ == '__main__':
#     app.run(debug = True)
"""


























