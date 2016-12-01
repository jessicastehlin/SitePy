# imports csv file from GASF website and prints results
# run time: approx. 15 minutes

import csv
import urllib

url = 'http://artiraq.org/static/opencontext/revised-tables/02f748469252f6d14250cb0c0b9d9f1e.csv'
response = urllib.urlopen(url)
cr = csv.reader(response) 

for row in cr:
    print row
