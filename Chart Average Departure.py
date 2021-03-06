"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
py.sign_in('crimsonreaper', 'jl1vyp4qt3')

def fetch_departure_2013():
    "Fetch and Return International Passenger Each Month From CSV File"
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2013 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2013":
            temporary.append(run[4])
            temporary.append(run[7])
            static_2013.append(temporary)
    return static_2013

def summary_departure_2013():
    "Return Summary Departure Passenger"
    departure_2013 = fetch_departure_2013()
    summary_2013 = {}
    for run in departure_2013:
        if run[0] in summary_2013:
            summary_2013[run[0]] += int(run[1])
        else:
            summary_2013[run[0]] = int(run[1])
    return summary_2013

def fetch_departure_2014():
    "Fetch and Return International Passenger Each Month From CSV File"
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2014 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2014":
            temporary.append(run[4])
            temporary.append(run[7])
            static_2014.append(temporary)
    return static_2014

def summary_departure_2014():
    "Return Summary Departure Passenger"
    departure_2014 = fetch_departure_2014()
    summary_2014 = {}
    for run in departure_2014:
        if run[0] in summary_2014:
            summary_2014[run[0]] += int(run[1])
        else:
            summary_2014[run[0]] = int(run[1])
    return summary_2014

def fetch_departure_2015():
    "Fetch and Return International Passenger Each Month From CSV File"
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2015 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2015":
            temporary.append(run[4])
            temporary.append(run[7])
            static_2015.append(temporary)
    return static_2015

def summary_departure_2015():
    "Return Summary Departure Passenger"
    departure_2015 = fetch_departure_2015()
    summary_2015 = {}
    for run in departure_2015:
        if run[0] in summary_2015:
            summary_2015[run[0]] += int(run[1])
        else:
            summary_2015[run[0]] = int(run[1])
    return summary_2015

def month_list():
    "Create Month list"
    departure_2013 = fetch_departure_2013()
    month = []
    for run in range(0, 13):
        month.append(departure_2013[run][0])
    return month

def average_departure():
    "Create List of Average Amount Departure Passenger Years 2013-2015"
    summary_2013 = summary_departure_2013()
    summary_2014 = summary_departure_2014()
    summary_2015 = summary_departure_2015()
    month = month_list()
    average_dpt = []
    temporary = 0
    for run in month:
        temporary = 0
        temporary = (int(summary_2013[run]) + int(summary_2014[run]) + int(summary_2015[run]))//3
        average_dpt.append(temporary)
    return average_dpt

def chart_average_departure():
    "Create Chart Amount Average Departure International Passenger Years 2013-2015"
    average_dpt = average_departure()
    month = month_list()
    trace0 = go.Bar(
        x=[run for run in month],
        y=[run for run in average_dpt],
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
        title='Average International Passengers Departure per Month 2013-2015',
    )
    fig = go.Figure(data=data, layout=layout)
    return py.plot(fig, filename='Average International Passengers Departure per Month 2013-2015')

tls.embed(chart_average_departure())
