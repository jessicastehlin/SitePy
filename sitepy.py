# imports csv file from GASF website and prints only Hall County data
# run time: less than 1 minute

import csv
import urllib

url = 'http://artiraq.org/static/opencontext/revised-tables/02f748469252f6d14250cb0c0b9d9f1e.csv'
response = urllib.urlopen(url)
cr = csv.reader(response) 

for row in cr:
    desiredCounty = 'Hall' # can change desiredCounty as needed
    county = row[15] # if changing desiredCounty, also change row[#]
    if county == desiredCounty:
        print row
