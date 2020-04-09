#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:22:07 2020

@author: thecassion
"""

import xmltodict
import json
import pandas as pd

json_filename="columns.json"
xlsx_filename="columns.xlsx"
xml_filename="aegZY7UbCcJUgcowLw5Gaj.xml"
writer = pd.ExcelWriter(xlsx_filename, engine='xlsxwriter')
with open(xml_filename) as xml_file:
    my_dict=xmltodict.parse(xml_file.read())
xml_file.close()
json_data=json.dumps(my_dict)


with open(json_filename, 'w') as outfile:
    json.dump(my_dict,outfile, indent=4, sort_keys=True)


body = my_dict["h:html"]["h:body"]
df_body = dict()
for key in body.keys():
    if type(body[key]) is list:
        df_body[key]=pd.DataFrame.from_dict(body[key])
        df_body[key].to_excel(writer, sheet_name=key)


writer.save()