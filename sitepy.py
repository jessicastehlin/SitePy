# module run time: less than 1 minute

import csv
import urllib

# open GASF file from url and save as csv
urllib.urlretrieve('http://artiraq.org/static/opencontext/revised-tables/02f748469252f6d14250cb0c0b9d9f1e.csv' , "gasf_sitepy.csv")

# filter only Hall County data and save to new output file
with open('gasf_sitepy.csv','r') as i, open('gasf_hall.csv','w') as o:
    r = csv.reader(i)
    w = csv.writer(o)
    for row in r:
        if row[15] == 'Hall':
            w.writerow(row)
