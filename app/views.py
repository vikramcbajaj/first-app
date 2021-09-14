# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound
import pandas as pd
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

@app.route('/users')
def users():
    df=pd.read_csv('app/dash_data/active_subs.csv')
    df_plan_wise = df.groupby(['exchange','name']).agg({'users':'sum'}).reset_index()
    datasets = []
    plans= ['Starter','Retail','Retail+','Creator','Creator+']
    colours = ['#FF4500','#D2691E','#00BFFF','#66CDAA','#FFA500']
    counter = 0
    ds=[]
    for i in list(df['exchange'].unique()):
        points=[]
        for j in plans:    
            points.append(str(df[(df['exchange']==i) & (df['name']==j)].users.sum()))
        ds.append({'label':i,
        'data': points,
        'backgroundColor': colours[counter]})
        counter+=1
    users = {'labels':plans,
             'datasets': ds} 
    datasets = []
    plan_types= ['Monthly','Quarterly','Yearly']
    colours = ['#00BFFF','#66CDAA','#FFA500','#FF4500','#D2691E']
    counter = 0
    ds2=[]
    for i in plans:
        points=[]
        for j in plan_types:    
            points.append(str(df[(df['name']==i) & (df['sub_type']==j)].users.sum()))
        ds2.append({'label':i,
        'data': points,
        'backgroundColor': colours[counter]})
        counter+=1
    sub_type = {'labels':plan_types,
             'datasets': ds2} 

    users_data = {'users':users,
                 'sub_type':sub_type}
    return json.dumps(users_data)


@app.route('/creators')
def creators():
    df = pd.read_pickle('dash_data/pm_invoices.pkl')
    
    return df


@app.route('/sales_data')
def sales_data():
    df = pd.read_pickle('dash_data/sales_data.pkl')
    return df


@app.route('/deployments')
def deployments():
    df = pd.read_pickle('dash_data/strats_report.pkl')
    return df




    