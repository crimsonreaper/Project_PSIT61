"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
py.sign_in('crimsonreaper', 'jl1vyp4qt3')

def fetch_arrive_2012():
    "Fetch and Return International Passenger Each Month From CSV File"
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2012 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2012":
            temporary.append(run[4])
            temporary.append(run[6])
            static_2012.append(temporary)
    return static_2012

def summary_arrive_2012():
    "Return Summary Arrive Passenger"
    arrive_2012 = fetch_arrive_2012()
    summary_2012 = {}
    for run in arrive_2012:
        if run[0] in summary_2012:
            summary_2012[run[0]] += int(run[1])
        else:
            summary_2012[run[0]] = int(run[1])
    return summary_2012

def fetch_arrive_2013():
    "Fetch and Return International Passenger Each Month From CSV File"
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2013 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2013":
            temporary.append(run[4])
            temporary.append(run[6])
            static_2013.append(temporary)
    return static_2013

def summary_arrive_2013():
    "Return Summary Arrive Passenger"
    arrive_2013 = fetch_arrive_2013()
    summary_2013 = {}
    for run in arrive_2013:
        if run[0] in summary_2013:
            summary_2013[run[0]] += int(run[1])
        else:
            summary_2013[run[0]] = int(run[1])
    return summary_2013

def fetch_arrive_2014():
    "Fetch and Return International Passenger Each Month From CSV File"
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2014 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2014":
            temporary.append(run[4])
            temporary.append(run[6])
            static_2014.append(temporary)
    return static_2014

def summary_arrive_2014():
    "Return Summary Arrive Passenger"
    arrive_2014 = fetch_arrive_2014()
    summary_2014 = {}
    for run in arrive_2014:
        if run[0] in summary_2014:
            summary_2014[run[0]] += int(run[1])
        else:
            summary_2014[run[0]] = int(run[1])
    return summary_2014

def month_list():
    "Create Month list"
    arrive_2012 = fetch_arrive_2012()
    month = []
    for run in range(0, 13):
        month.append(arrive_2012[run][0])
    return month

def average_arrive():
    "Create List of Average Amount Arrive Passenger Years 2012-2014"
    summary_2012 = summary_arrive_2012()
    summary_2013 = summary_arrive_2013()
    summary_2014 = summary_arrive_2014()
    month = month_list()
    average_arv = []
    temporary = 0
    for run in month:
        temporary = 0
        temporary = (int(summary_2012[run]) + int(summary_2013[run]) + int(summary_2014[run]))//3
        average_arv.append(temporary)
    return average_arv

def chart_average_arrive():
    "Create Chart Amount Average Arrive International Passenger Years 2012-2014"
    average_arv = average_arrive()
    month = month_list()
    trace0 = go.Bar(
        x=[run for run in month],
        y=[run for run in average_arv],
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5,
            )
        ),
        opacity=0.6
    )
    data = [trace0]
    layout = go.Layout(
        title='Average International Passengers Arrive per Month 2012-2014',
    )
    fig = go.Figure(data=data, layout=layout)
    return py.plot(fig, filename='Average International Passengers Arrive per Month 2012-2014')

tls.embed(chart_average_arrive())
