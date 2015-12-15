# 6. AVERAGE NUMBERS
#
# Assume that a file containing a series of integers is named
# 'numbers.txt' and exists on the computer's disk. Write a
# program that reads all of the numbers stored in the file
# and calculates their total.

def main():
    try:
        file = open("numbers.txt", "r")
        num = file.readlines()
        file.close()
    except IOError:
        print("IOError, something is wrong with your file")
        
    
    get_avg(num)
    
    
    
def get_avg(num): 
    total = 0
    try:
        num = list(map(int, num))
    except ValueError:
        print("The values are not converted to a number!" )
    for x in num:
        total += x
    print("The total amount is", total,"and the average is", total/len(num))
    
        
          
main()


 