#this program writes three lines of data to a file
def main():
   outfile = open('philosophers.txt','w')
   outfile.write('John Locke' + "\n")
   outfile.write('David Hume' + "\n")
   # or write it like this outfile.write('David Hum/n')
   outfile.write('Edmund Burke' + "\n")
   #close file
   outfile.close
#call main function
main()