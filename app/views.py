# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound

# App modules
from app import app
import dash_inputs
import json

# App main route + generic routing
@app.route('/')
def index():
    try:
        daily = get_daily_data()
        inv_data = dash_inputs.chart_data(dash_inputs.sample_inv(),'invoice_type','amount')
        return render_template( 'index.html', daily=daily,inv_data=inv_data)
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


   

@app.route('/sales')
def sales():
    
    try:

        # Detect the current page
        inv_data = dash_inputs.chart_data(dash_inputs.sample_inv(),'invoice_type','amount')

        # Serve the file (if exists) from app/templates/FILE.html
        return json.dumps(inv_data)
    
    except TemplateNotFound:
        return render_template('page-404.html'), 404
'''
def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  
   
'''