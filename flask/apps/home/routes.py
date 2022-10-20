# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from re import S
from apps.home import blueprint
from apps.streamsChartsScrapper import streamsChartsScrapperAPI
from flask import render_template, request, Flask, redirect, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound
import pandas as pd
import json, os, csv


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template('home/' + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

@blueprint.route('/tableGenerator', methods = ['POST'])
def generateTable():
    if request.method == 'POST':
        if request.files:
            for fileID in request.files:
                f = request.files[fileID]
                # Checks if file does not end .csv
                if not f.filename.endswith('.csv'):
                    return('Method Not Allowed', 504)
                return(pd.read_csv(f).to_json())
        elif 'filteredList' in request.form:
            filteredLst = request.form['filteredList'].split(',')
            # Dict String to Dict to Json to Dataframe to HTML with filtered rows
            filterDF = pd.read_json(json.dumps(json.loads(request.form['csvData'])))[filteredLst]
            return({"html": filterDF.to_html(justify='left', index=False), "csv": filterDF.to_csv(index=False)})
        return redirect(request.referrer)

@blueprint.route('/chartGenerator', methods = ['POST'])
def generateCharts():
    platformType = request.get_data(as_text=True)
    # Get the list of csv files
    listOfCSV = []
    for file in os.listdir("apps/graphsExcel/"):
        if file.lower().endswith(".csv"):
            if file.lower().startswith(platformType):
                listOfCSV.append(file)
            elif file.lower().startswith(platformType):
                listOfCSV.append(file)

    # Setup strings for creating html table
    chartHTML = ''
    chartSettings = []
    chartId = 0
    cardDiv = 1
    bodyTwoCard = '<div class="row mt--2">'
    mediumCardBody = ['<div class="col-md-6"><div class="card full-height"><div class="card-body"><div class="card-title">',
                        '</div><br><div class="chart-container"><canvas id=chart',
                        '></canvas></div></div></div></div>']

    for csvFile in listOfCSV:
        csvFileSplit = csvFile[:-4].split('_')
        # Makes a new div that supports two cards
        if cardDiv == 1:
            chartHTML += bodyTwoCard
        chartHTML += mediumCardBody[0] + csvFileSplit[2] + mediumCardBody[1] + str(chartId) + mediumCardBody[2]
        if cardDiv == 2:
            chartHTML += '</div>'
            cardDiv = 0
        cardDiv += 1
        chartId += 1

        # Generate the settings for the graphs
        with open('apps/graphsExcel/' + csvFile, mode='r') as f:
            csvDict = csv.reader(f)
            match csvFileSplit[1]:
                case 'line':
                    chartSettings.append(generateLineChart(csvDict))
                case 'bar':
                    chartSettings.append(generateBarChart(csvDict))

    return({"chartSettings": chartSettings, "htmlBody": chartHTML})

def generateLineChart(csvDict):
    csvRowX = []
    csvRowY = []
    for csvRow in csvDict:
        csvRowX.append(csvRow[0])
        csvRowY.append(csvRow[1])
    chartLabel = csvRowY[0]
    csvRowX.pop(0)
    csvRowY.pop(0)

    myLineChart = {
        'type': 'line',
        'data': {
            'labels': csvRowX,
            'datasets': [{
                'label': chartLabel,
                'borderColor': "#1d7af3",
                'pointBorderColor': "#FFF",
                'pointBackgroundColor': "#1d7af3",
                'pointBorderWidth': 2,
                'pointHoverRadius': 4,
                'pointHoverBorderWidth': 1,
                'pointRadius': 4,
                'backgroundColor': 'transparent',
                'fill': 'true',
                'borderWidth': 2,
                'data': csvRowY
            }]
        },
        'options' : {
            'responsive': 'true', 
            'maintainAspectRatio': 'false',
            'legend': {
                'position': 'bottom',
                'labels' : {
                    'padding': 10,
                    'fontColor': '#1d7af3',
                }
            },
            'tooltips': {
                'bodySpacing': 4,
                'mode':"nearest",
                'intersect': 0,
                'position':"nearest",
                'xPadding':10,
                'yPadding':10,
                'caretPadding':10
            },
            'layout':{
                'padding':'{left:15,right:15,top:15,bottom:15}'
            }
        }
    }
    return myLineChart

def generateBarChart(csvDict):
    csvRowX = []
    csvRowY = []
    for csvRow in csvDict:
        csvRowX.append(csvRow[0])
        csvRowY.append(csvRow[1])
    chartLabel = csvRowY[0]
    csvRowX.pop(0)
    csvRowY.pop(0)

    myBarChart = {
        'type': 'bar',
        'data': {
            'labels': csvRowX,
            'datasets' : [{
                'label': chartLabel,
                'backgroundColor': 'rgb(23, 125, 255)',
                'borderColor': 'rgb(23, 125, 255)',
                'data': csvRowY,
            }],
        },
        'options': {
            'responsive': 'true', 
            'maintainAspectRatio': 'false',
            'scales': {
                'yAxes': [{
                    'ticks': {
                        'beginAtZero': 'true'
                    }
                }]
            },
        }
    }
    return myBarChart

@blueprint.route('/streamsChartScrap', methods = ['POST'])
def steamChartScrap():
    csvOutput = streamsChartsScrapperAPI.get_top_twitch_streamers(request.form['clientID'], request.form['tokenKey'])
    csvToDF = pd.read_json(json.dumps(csvOutput))

    return csvToDF.to_csv(index=False)

# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
