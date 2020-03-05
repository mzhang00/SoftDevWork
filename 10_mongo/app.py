#teamRAM - Michael Zhang and Amanda Chen
#SoftDev pd1
#K10: Import/Export Bank
#2020-03-02

from pymongo import MongoClient
from bson.json_util import loads
from pprint import pprint

client = MongoClient('localhost')
db = client.RAM
meteors = db.meteors

if (meteors in db.list_collection_names()):
    f = open("meteorites.json","r")
    rString = f.readlines()
    t = loads(rString)

def filter_mass(mass):
    return list(col.find({'mass':mass}))

def filter_coords(longitude, lat):
    return list(col.find({'reclong':longitude, 'reclat': lat}))

def filter_class(recclass):
    return list(col.find({'recclass':recclass}))

def filter_year(year):
    return list(col.find({'year':year}))
