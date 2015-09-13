#!/bin/bash

scrapy crawl contracthireandlease -o db/cars-$(date +%s).json

#mongoimport -h localhost --db chal --collection cars db/cars-1442071840.json --jsonArray
#echo -e 'use chal\ndb.cars.find({"i_manufacturer":"audi","i_model":"a4"}).pretty()' | mongo


