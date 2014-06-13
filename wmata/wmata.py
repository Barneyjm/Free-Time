# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 13:02:26 2014

@author: James
"""
import json
from bs4 import BeautifulSoup
import urllib2
import subprocess

from pymongo import MongoClient
    
try:
    subprocess.Popen(['C:\/mongodb\/bin\/mongod'])
except:
    print "Failed to launch database--please try again or manually initiate."
    
client = MongoClient('localhost', 27017)
wmata = client.wmata_database
stations = wmata.stations_collection


def fetch_stations():
    page = urllib2.urlopen('http://api.wmata.com/Rail.svc/json/jStations?api_key=57y6m5a6xarurh3xqfwu74sr')

    for line in page:
        st = json.loads(line)
    
    return st
    
def insert_stations(st):
    for val in st.values():
        for ind in val:
            print "inserting:"
            print type(ind)
            print ind
            try:
                stations.insert(ind)
            except:
                print "not inserted..."
                
def get_station_codes(prefix):
    codes = []
    for station in stations.find({"Code":*):
        print station
        codes.append(station['Code'])
        
    return codes
        
                
def fetch_predictions(station_codes):
    page = urllib2.urlopen('http://api.wmata.com/StationPrediction.svc/json/GetPrediction/' + station_codes + '?api_key=57y6m5a6xarurh3xqfwu74sr')
    for line in page:
        pred = json.loads(line)
        
    return pred
    
def insert_predictions():
    pass

st = fetch_stations()

cd = get_station_codes("A")

#insert_stations(st)

#print stations