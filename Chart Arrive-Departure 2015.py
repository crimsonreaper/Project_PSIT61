"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
py.sign_in('crimsonreaper', 'jl1vyp4qt3')

def fetch_arrive_2015():
    "Fetch and Return International Passenger Each Month From CSV File"
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2015 = []
    for run in static:
        temporary = []
        if run[1] == "Passenger" and run[2] == "International" and run[3] == "2015":
            temporary.append(run[4])
            temporary.append(run[6])
            static_2015.append(temporary)
    return static_2015

def summary_arrive_2015():
    "Return Summary Arrive Passenger"
    arrive_2015 = fetch_arrive_2015()
    summary_2015 = {}
    for run in arrive_2015:
        if run[0] in summary_2015:
            summary_2015[run[0]] += int(run[1])
        else:
            summary_2015[run[0]] = int(run[1])
    return summary_2015

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
    arrive_2015 = fetch_arrive_2015()
    month = []
    for run in range(0, 13):
        month.append(arrive_2015[run][0])
    return month

def chart_arv_dpt_2015():
    "Create Chart Amount Arrive and Departure International Passenger Years 2015"
    summary_arv = summary_arrive_2015()
    summary_dpt = summary_departure_2015()
    month = month_list()
    trace0 = go.Bar(
        x=[run for run in month],
        y=[summary_arv[run] for run in month],
        name='Arrive',
        marker=dict(
            color='rgb(49,130,189)'
        )
    )
    trace1 = go.Bar(
        x=[run for run in month],
        y=[summary_dpt[run] for run in month],
        name='Departure',
        marker=dict(
            color='rgb(204,204,204)',
        )
    )
    data = [trace0, trace1]
    layout = go.Layout(
        title='International Passengers Arrive/Departure per Month - 2015',
        xaxis=dict(
            tickangle=-45,
        ),
        barmode='group',
    )
    fig = go.Figure(data=data, layout=layout)
    return py.plot(fig, filename='International Passengers Arrive/Departure per Month - 2015')

tls.embed(chart_arv_dpt_2015())
