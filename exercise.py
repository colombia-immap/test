# -*- coding: utf-8 -*-
import csv
import json

file = open('cities_test', 'r')
cadena = file.read()
ob_json = json.loads(cadena)
print ob_json[0]