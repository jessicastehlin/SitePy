# SitePy

## Project Objective
SitePy is a Python program that I created for my final project in my "Python Programming for GIS" class. The purpose of this program is to help me to quickly and efficiently import archaeological site data from an online database (delivered as a csv file), and pull out specific data for analysis.

I first came up for the idea for this project when I found a data file containing information about archaeological sites throughout the state of Georgia. I have been interested in archaeology for quite a while, and I had been hoping to find a similar dataset online, which I planned to use to create archaeological maps using GIS. However, when I downloaded the file and began to look through the data it contained, I quickly realized that the sheer amount of data in the file was very difficult to sort through. (The file was 47 fields long, and included data for over 5,000 sites.) Additionally, I knew that I would not require all of the information in the file to make the maps I was interested in. For this reason, I decided to create a Python module that would allow for easy organization and management of the data.

Although this project began as a way for me to deal with the archaeological data file that I found, I quickly realized that it would be beneficial to create a program that could be easily customized for use with other large datasets. For this reason, I made a conscious effort to ensure that each section of code could be edited to manage different datasets. Therefore, although the code in this repository is specifically geared towards my site data (linked in the "Data" section below), it could easily be altered to filter information in other csv files. 

## Data
The downloaded data for this project comes from the Georgia Archaeological Site File (GASF), and is available for free download through [opencontext.org](https://opencontext.org/). The GASF is based at the University of Georgia's [Laboratory of Archaeology](https://archaeology.uga.edu/archlab/), and it was founded in 1976. The GASF is "the official repository for Georgia’s archaeological site information", and maintains detailed records of all archaeological sites throughout the state of Georgia.

The data file for this project can be downloaded [here](https://opencontext.org/tables/02f748469252f6d14250cb0c0b9d9f1e) as a csv file. The csv file includes 47 fields and 53,190 rows, and the size of the file is 53,429 KB. At the data download page, the file is described as being "the main dataset describing sites documented by the Georgia State SHPO". 

## Program Details

### Step 1: Open GASF file from url and save as a csv file.
The first (and most integral) step in this Python module is to successfully download the data and save it as a csv file to your personal computer. For the SitePy program, I was downloading the GASF data from [this link](https://opencontext.org/tables/02f748469252f6d14250cb0c0b9d9f1e). I also created a new folder on my computer's U: drive, where I saved all of the output files for this project.

To download the csv file from the GASF website, I used the urllib module; specifically, urllib.urlretrieve. The Python docs for urllib.urlretrieve can be found [here](https://docs.python.org/2/library/urllib.html#urllib.urlretrieve).

The following code downloads and saves the GASF data:
```python
urllib.urlretrieve('http://artiraq.org/static/opencontext/revised-tables/02f748469252f6d14250cb0c0b9d9f1e.csv' , "gasf_sitepy.csv")
```

### Step 2: Filter specific data and save to new output file.
This step can be repeated multiple times within the code, depending on how many different ways you need to filter the data. In the example shown below, I will filter only the Hall County site data, and save the result to a new csv file. It is also important to specify whether you want to write the field headings in the output file as well; if you do not specify, Python will only write the data contained within each field.

The output file for the filtered data will be saved in the same location as the original downloaded file. If you would like to save the code to a different folder or drive, you would need to write additional code to do so.
```python
with open('gasf_sitepy.csv','r') as i, open('gasf_hall.csv','w') as o:
    r = csv.reader(i)
    w = csv.writer(o)
    for row in r:
        if row[15] == 'Hall' or row[15] == 'Context (3)': # 'Context (3)' is the field heading
            w.writerow(row)
```

### Step 3: Count total number of sites in a given category
In many cases, it can be useful to be able to quickly determine the number of archaeological sites in a given category, without needing to go through the data and count the items manually. This section of the code does not produce an output file; instead, it reads the original data file and counts the number of items in a specified category, printing the result.

To print the total number of Hall County sites, I would use the code below:
```python
my_reader = csv.reader(open('gasf_sitepy.csv'))
ctr = 0
for record in my_reader:
    if record[15] == 'Hall':
        ctr += 1
print 'Number of Hall County sites: %s' %(ctr)
```

## References (Links)
### Georgia Archaeological Site File (GASF)
- [Georgia Archaeological Site File (GASF) website homepage](https://archaeology.uga.edu/gasf/home)
- [GASF project page at the Open Context website](https://opencontext.org/projects/64013C33-4039-46C9-609A-A758CE51CA49)
- [Direct link to GASF data download page (csv file)](https://opencontext.org/tables/02f748469252f6d14250cb0c0b9d9f1e)

### Python Docs
- [urllib module](https://docs.python.org/2/library/urllib.html)
  - [urllib.urlretrieve](https://docs.python.org/2/library/urllib.html#urllib.urlretrieve)
- [csv module](https://docs.python.org/2/library/csv.html#)
  - [csv.reader](https://docs.python.org/2/library/csv.html#csv.reader)
  - [csv.writer](https://docs.python.org/2/library/csv.html#csv.writer)

### Other Resources
- [Georgia Department of Natural Resources - Historic Preservation Division (SHPO) website](http://www.georgiashpo.org/)
