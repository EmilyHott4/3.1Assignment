import csv
infile = open('employeepay.csv','r')
csvfile = csv.reader(infile,delimiter=',')

next(csvfile)
for record in csvfile:
    print('Employee ID:',record[0])
    print('Employee First Name:',record[1])
    print('Employee Last Name:',record[2])
    print('Employee Salary:',record[3])
    print('Employee Bonus:',record[4])

    input()

    
    