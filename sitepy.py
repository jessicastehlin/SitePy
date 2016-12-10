# module run time: approx. 1 minute

import csv
import urllib

# open GASF file from url and save as csv
urllib.urlretrieve('http://artiraq.org/static/opencontext/revised-tables/02f748469252f6d14250cb0c0b9d9f1e.csv' , "gasf_sitepy.csv")

# filter only Hall County data and print results
with open('gasf_sitepy.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[15] == 'Hall':
            print row
