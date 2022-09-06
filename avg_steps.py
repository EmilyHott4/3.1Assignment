import csv
infile = open('steps.csv','r')
csvfile = csv.reader(infile,delimiter=',')
next(csvfile)

total_steps = 0
counter = 1
month = 1


for record in csvfile:
    if record[0] = 1:
        #float(record[0])
        steps = int(record[1])
        total_steps += steps
        counter += 1
    else:
        avg_steps = total_steps/counter
        January = 1 
        February = 2 
        print()
        print()


    #while month = 1:
        #total_steps = 


    

    counter +=  1
    month += 1
