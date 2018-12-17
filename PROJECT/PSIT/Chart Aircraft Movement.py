"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
def fetch_data():
    """Return list from fetch data csv"""
    import csv
    main_data = csv.reader(open('airtrafficstats.csv', newline=''))
    main_data = [row for row in main_data]
    print(main_data)
    '''return main_data

def airmove_airport():
    """Return list of data about total aircraft movement"""
    data = fetch_data()
    bkk = quarter_stat('BKK', data)
    cnx = quarter_stat('CNX', data)
    hkt = quarter_stat('HKT', data)
    return [bkk, cnx, hkt]

def quarter_stat(airport, data):
    """Return list of quarter data"""
    year = [0, 0, 0, 0]
    stat = []
    locate = 0
    count = 0
    for i in data:
        if i[0] == airport and i[1] == 'Flight':
            year[locate] += (int(i[6]) + int(i[7]))
            count += 1
        if count % 3 == 0 and count != 0:
            locate += 1
        if count % 12 == 0 and count != 0:
            locate = 0
        if count % 24 == 0 and count != 0:
            for i in year:
                stat.append(i)
            year = [0, 0, 0, 0]
            locate = 0
            count = 0
    return stat

def plot_aircraft_per_month():
    import plotly.plotly as py
    import plotly.graph_objs as go
    py.sign_in('iamplaster', '0ivoxihbxn')

    bkk, dmk, cnx, hkt = airmove_airport()
    trace1 = go.Scatter(
        x=[1, 2, 3, 4, 5, 
           6, 7, 8, 9, 10,
           11, 12],
        y=bkk,
        name = 'Suvarnabhumi airport',
        connectgaps=True
    )
    trace2 = go.Scatter(
        x=[1, 2, 3, 4, 5, 
           6, 7, 8, 9, 10,
           11, 12],
        y=cnx,
        name = 'Chiang Mai airport',
        connectgaps=True
    )
    trace3 = go.Scatter(
        x=[1, 2, 3, 4, 5, 
           6, 7, 8, 9, 10,
           11, 12],
        y=hkt,
        name = 'Phuket airport',
        connectgaps=True
    )

    data = [trace1, trace2, trace3]
    layout = dict(title = 'Aircraft Movement per quarter 2013 - 2015',
                  xaxis = dict(title = 'Passenger'),
                  yaxis = dict(title = 'Quarter'),
                  )

    fig = dict(data=data, layout=layout)
    return py.iplot(fig, filename='simple-connectgaps')
    
plot_aircraft_per_month()'''
fetch_data()
