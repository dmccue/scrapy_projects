#!/usr/bin/python

import json,sys

json_data = ""
with open('db/cars.json') as json_file:
    json_data = json.load(json_file)

print json_data[0].keys()

json_data = sorted(json_data, key=lambda k: k['i_manufacturer'], reverse=False)
#[u'i_manufacturer', u'i_url', u'i_model', u'i_contract_initial', u'i_contract_monthlyprice', u'i_contract_term', u'i_desc', u'i_contract_mileage']


for line in json_data:
    print line['i_manufacturer'] + "," + \
    line['i_model'] + "," + \
    line['i_desc'] + "," + \
    line['i_contract_term'] + "*" + line['i_contract_monthlyprice'] + "," + \
    line['i_contract_mileage'][:-3] + 'k'
