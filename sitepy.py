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
        if row[15] == 'Hall' or row[15] == 'Context (3)':
            w.writerow(row)

# filter only Endangered sites and save to new output file

with open('gasf_sitepy.csv','r') as i, open('gasf_endangered.csv','w') as o:
    r = csv.reader(i)
    w = csv.writer(o)
    for row in r:
        if row[36] == 'Endangered' or row[36] == 'Preservation Prospects':
            w.writerow(row)

# count total number of Hall County sites

my_reader = csv.reader(open('gasf_sitepy.csv'))
ctr = 0
for record in my_reader:
    if record[15] == 'Hall':
        ctr += 1
print 'Number of Hall County sites: %s' %(ctr)
