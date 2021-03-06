# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# import Flask 
from flask import Flask

# Inject Flask magic
app = Flask(__name__)

# App Config - the minimal footprint
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True 
app.config['SECRET_KEY'] = 'S#perS3crEt_JamesBond' 
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Import routing to render the pages
from app import views
