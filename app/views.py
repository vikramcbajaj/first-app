# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound

# App modules
from app import app

# App main route + generic routing
@app.route('/')
def index():
    try:
        daily = get_daily_data()
        return render_template( 'index.html', daily=daily)
    except exception(e):
        print(e)
        return

def get_daily_data():
    daily = {}
    daily['new_users']=900
    daily['user_logins']=5000
    daily['new_deployments']=1200
    daily['new_strategies']=125
    return daily


   
'''
@app.route('/sales')
def sales(path):
    
    try:

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template( path, segment=segment )
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404

def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
   
'''