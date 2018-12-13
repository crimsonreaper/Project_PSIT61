"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
import csv
def fetch_data_2015():
    static = open("airtrafficstats.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2015 = []
    for run in static:
        if run[3] == "2015":
            static_2015.append(run)
    return static_2015

def fetch_data_2014():
    static = open("airtrafficstats.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2014 = []
    for run in static:
        if run[3] == "2014":
            static_2014.append(run)
    return static_2014

def fetch_data_2013():
    static = open("airtrafficstats.csv", newline="")
    data = csv.reader(static)
    static = [run for run in data]
    static_2013 = []
    for run in static:
        if run[3] == "2013":
            static_2013.append(run)
    return static_2013
  
def ranking(d_stat):
    """Return cities that ranked"""
    name = sorted(d_stat, key=d_stat.get)
    amount = sorted(list(d_stat.values()))
    stat = []
    pre_stat = []
    for i in range(len(name)):
        pre_stat.append(name[i])
        pre_stat.append(amount[i])
        stat.append(pre_stat)
        pre_stat = []
    return stat

def merge(stat_1, stat_2):
    """Return dic that merge form two dic"""
    stat = {}
    for i in list(stat_1):
        stat[i] = stat_1[i] + stat_2[i]
    return stat
