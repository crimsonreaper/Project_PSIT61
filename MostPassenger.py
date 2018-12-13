"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
def fetch_data_2015():
    """For import data year 2015 from excel"""
    static = open("airtraffic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2015 = []
    for run in static:
        if run[3] == "2015":
            static_2015.append(run)
    return static_2015

def fetch_data_2014():
    """For import data year 2014 from excel"""
    static = open("airtraffic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2014 = []
    for run in static:
        if run[3] == "2014":
            static_2014.append(run)
    return static_2014

def fetch_data_2013():
    """For import data year 2013 from excel"""
    static = open("airtraffic.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2013 = []
    for run in static:
        if run[3] == "2013":
            static_2013.append(run)
    return static_2013

def bkk_airport_2013():
    """Find the number of the passenger in BKK airport in year 2013."""
    num_0 = 0
    for i in fetch_data_2013():
        if i[0] == "BKK":
            num_0 += int(i[6])
    return num_0

def cnx_airport_2013():
    """Find the number of the passenger in CNX airport in year 2013."""
    num_0 = 0
    for i in fetch_data_2013():
        if i[0] == "CNX":
            num_0 += int(i[6])
    return num_0

def hkt_airport_2013():
    """Find the number of the passenger in HKT airport in year 2013."""
    num_0 = 0
    for i in fetch_data_2013():
        if i[0] == "HKT":
            num_0 += int(i[6])
    return num_0

def bkk_airport_2014():
    """Find the number of the passenger in BKK airport in year 2014."""
    num_0 = 0
    for i in fetch_data_2014():
        if i[0] == "BKK":
            num_0 += int(i[6])
    return num_0

def cnx_airport_2014():
    """Find the number of the passenger in CNX airport in year 2014."""
    num_0 = 0
    for i in fetch_data_2014():
        if i[0] == "CNX":
            num_0 += int(i[6])
    return num_0

def hkt_airport_2014():
    """Find the number of the passenger in HKT airport in year 2014."""
    num_0 = 0
    for i in fetch_data_2014():
        if i[0] == "HKT":
            num_0 += int(i[6])
    return num_0

def bkk_airport_2015():
    """Find the number of the passenger in BKK airport in year 2015."""
    num_0 = 0
    for i in fetch_data_2015():
        if i[0] == "BKK":
            num_0 += int(i[6])
    return num_0

def cnx_airport_2015():
    """Find the number of the passenger in CNX airport in year 2015."""
    num_0 = 0
    for i in fetch_data_2015():
        if i[0] == "CNX":
            num_0 += int(i[6])
    return num_0

def hkt_airport_2015():
    """Find the number of the passenger in HKT airport in year 2015."""
    num_0 = 0
    for i in fetch_data_2015():
        if i[0] == "HKT":
            num_0 += int(i[6])
    return num_0
hkt_airport_2015()

def bkk_airport():
    """Find the result of BKK airport"""
    return ('%.0f' %((bkk_airport_2013()+bkk_airport_2014()+bkk_airport_2015())/3))

def cnx_airport():
    """Find the result of CNX airport"""
    return ('%.0f' %((cnx_airport_2013()+cnx_airport_2014()+cnx_airport_2015())/3))

def hkt_airport():
    """Find the result of HKT airport"""
    return ('%.0f' %((hkt_airport_2015()+hkt_airport_2015()+hkt_airport_2015())/3))

def prin_data():
    """For print the most number of data."""
    if and bkk_airport() > cnx_airport() and bkk_airport() > hkt_airport():
        print("BKK", bkk_airport())
    elif cnx_airport() > hkt_airport():
        print("CNX", cnx_airport())
    else:
        print("HKT", airport())

prin_data()
