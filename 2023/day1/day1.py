print('hello world')
import sys
# read in file, command line arg for file name
file = open(sys.argv[1]).read().strip()
# initialize lists of all first and second digits
d1 = []
d2 = []

for line in file.split('\n'):
    d1_digits = []
    # iterate through every position
    for i, alphanumeric in enumerate(line):
        # print(i, alphanumeric)
        if alphanumeric.isdigit():
            d1_digits.append(int(alphanumeric))
        for j, potentialalphabet in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']):
            if line[i:].startswith(potentialalphabet):
                # print(line[i:])
                d1_digits.append(j+1)
    number = d1_digits[0]*10 + d1_digits[-1]
    d1.append(number)
    # print(d1)
print (sum(d1))

        
