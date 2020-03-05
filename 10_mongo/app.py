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

if (meteors in db.list_meteorslection_names()):
    f = open("meteorites.json","r")
    rString = f.readlines()
    t = loads(rString)

def filter_mass(mass):
    return list(meteors.find({'mass':mass}))

def filter_coords(longitude, lat):
    return list(meteors.find({'reclong':longitude, 'reclat': lat}))

def filter_class(recclass):
    return list(meteors.find({'recclass':recclass}))

def filter_year(year):
    return list(meteors.find({'year':year}))
