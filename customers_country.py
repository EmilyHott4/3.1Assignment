import csv
infile = open('customers.csv','r')
outfile = open('customer_country.csv','w')
csvfile = csv.reader(infile,delimiter=',')

next(csvfile)

for record in csvfile:
    fname = record[1]
    lname = record[2]
    counrty = record[4]
    outfile.write(fname+' ' +lname,+country +\n)
    
    #outfile.write = (record[1],' ' record [2],','record[4])
    input()
outfile.close()
infile.close()
