"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
import plotly.tools as tls
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('crimsonreaper', 'jl1vyp4qt3')

def fetch_data_2015():
    """For import data year 2015 from excel"""
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2015 = []
    for run in static:
        if run[3] == "2015":
            static_2015.append(run)
    return static_2015

def fetch_data_2014():
    """For import data year 2014 from excel"""
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2014 = []
    for run in static:
        if run[3] == "2014":
            static_2014.append(run)
    return static_2014

def fetch_data_2013():
    """For import data year 2013 from excel"""
    static = open("airtraffict.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2013 = []
    for run in static:
        if run[3] == "2013":
            static_2013.append(run)
    return static_2013

def freight_jan_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "January":
            num_0 = i[6]
    return int(num_0)

def freight_feb_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "Febuary":
            num_0 = i[6]
    return int(num_0)

def freight_mar_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "March":
            num_0 = i[6]
    return int(num_0)

def freight_apr_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "April":
            num_0 = i[6]
    return int(num_0)

def freight_may_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "May":
            num_0 = i[6]
    return int(num_0)

def freight_june_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "June":
            num_0 = i[6]
    return int(num_0)

def freight_july_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "July":
            num_0 = i[6]
    return int(num_0)

def freight_aug_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "August":
            num_0 = i[6]
    return int(num_0)

def freight_sep_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "September":
            num_0 = i[6]
    return int(num_0)

def freight_oct_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "October":
            num_0 = i[6]
    return int(num_0)

def freight_nov_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "November":
            num_0 = i[6]
    return int(num_0)

def freight_dec_2013():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "December":
            num_0 = i[6]
    return int(num_0)

def freight_jan_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "January":
            num_0 = i[6]
    return int(num_0)

def freight_feb_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "Febuary":
            num_0 = i[6]
    return int(num_0)

def freight_mar_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "March":
            num_0 = i[6]
    return int(num_0)

def freight_apr_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "April":
            num_0 = i[6]
    return int(num_0)

def freight_may_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "May":
            num_0 = i[6]
    return int(num_0)

def freight_june_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2013():
        if i[1] == "Freight" and i[4] == "June":
            num_0 = i[6]
    return int(num_0)

def freight_july_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "July":
            num_0 = i[6]
    return int(num_0)

def freight_aug_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "August":
            num_0 = i[6]
    return int(num_0)

def freight_sep_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "September":
            num_0 = i[6]
    return int(num_0)

def freight_oct_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "October":
            num_0 = i[6]
    return int(num_0)

def freight_nov_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "November":
            num_0 = i[6]
    return int(num_0)

def freight_dec_2014():
    """Find the number of freight of the month"""
    for i in fetch_data_2014():
        if i[1] == "Freight" and i[4] == "December":
            num_0 = i[6]
    return int(num_0)

def freight_jan_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "January":
            num_0 = i[6]
    return int(num_0)

def freight_feb_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "Febuary":
            num_0 = i[6]
    return int(num_0)

def freight_mar_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "March":
            num_0 = i[6]
    return int(num_0)

def freight_apr_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "April":
            num_0 = i[6]
    return int(num_0)

def freight_may_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "May":
            num_0 = i[6]
    return int(num_0)

def freight_june_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "June":
            num_0 = i[6]
    return int(num_0)

def freight_july_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "July":
            num_0 = i[6]
    return int(num_0)

def freight_aug_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "August":
            num_0 = i[6]
    return int(num_0)

def freight_sep_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "September":
            num_0 = i[6]
    return int(num_0)

def freight_oct_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "October":
            num_0 = i[6]
    return int(num_0)

def freight_nov_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "November":
            num_0 = i[6]
    return int(num_0)

def freight_dec_2015():
    """Find the number of freight of the month"""
    for i in fetch_data_2015():
        if i[1] == "Freight" and i[4] == "December":
            num_0 = i[6]
    return int(num_0)

def freight_jan():
    """For find the result of January year 2013-2015"""
    num_0 = ('%0.f' %((freight_jan_2013()+freight_jan_2014()+freight_jan_2015())/3))
    return num_0

def freight_feb():
    """For find the result of Febuary year 2013-2015"""
    num_0 = ('%0.f' %((freight_feb_2013()+freight_feb_2014()+freight_feb_2015())/3))
    return num_0

def freight_mar():
    """For find the result of March year 2013-2015"""
    num_0 = ('%0.f' %((freight_mar_2013()+freight_mar_2014()+freight_mar_2015())/3))
    return num_0

def freight_apr():
    """For find the result of April year 2013-2015"""
    num_0 = ('%0.f' %((freight_apr_2013()+freight_apr_2014()+freight_apr_2015())/3))
    return num_0

def freight_may():
    """For find the result of May year 2013-2015"""
    num_0 = ('%0.f' %((freight_may_2013()+freight_may_2014()+freight_may_2015())/3))
    return num_0

def freight_june():
    """For find the result of June year 2013-2015"""
    num_0 = ('%0.f' %((freight_june_2013()+freight_june_2014()+freight_june_2015())/3))
    return num_0

def freight_july():
    """For find the result of July year 2013-2015"""
    num_0 = ('%0.f' %((freight_july_2013()+freight_july_2014()+freight_july_2015())/3))
    return num_0

def freight_aug():
    """For find the result of August year 2013-2015"""
    num_0 = ('%0.f' %((freight_aug_2013()+freight_aug_2014()+freight_aug_2015())/3))
    return num_0

def freight_sep():
    """For find the result of September year 2013-2015"""
    num_0 = ('%0.f' %((freight_sep_2013()+freight_sep_2014()+freight_sep_2015())/3))
    return num_0

def freight_oct():
    """For find the result of October year 2013-2015"""
    num_0 = ('%0.f' %((freight_oct_2013()+freight_oct_2014()+freight_oct_2015())/3))
    return num_0

def freight_nov():
    """For find the result of November year 2013-2015"""
    num_0 = ('%0.f' %((freight_nov_2013()+freight_nov_2014()+freight_nov_2015())/3))
    return num_0

def freight_dec():
    """For find the result of December year 2013-2015"""
    num_0 = ('%0.f' %((freight_dec_2013()+freight_dec_2014()+freight_dec_2015())/3))
    return num_0

def prin_graph():
    """For print graph of result"""
    data = [
            go.Bar(
            x = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July',\
               'August', 'September', 'October', 'November', 'December'],
            y = [freight_jan(), freight_feb(), freight_mar(), freight_apr(),\
                 freight_may(), freight_june(), freight_july(), freight_aug(),\
                 freight_sep(), freight_oct(), freight_nov(), freight_dec()]
        )
    ]
    return py.plot(data, filename='basic-bar')

tls.embed(prin_graph())
