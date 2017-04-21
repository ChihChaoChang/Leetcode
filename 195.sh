'''
Tenth Line
How would you print just the 10th line of a file?

For example, assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

Your script should output the tenth line, which is: 

Line 10
'''

awk '{if(NR==10) print $0}' file.txt 
# First

awk "NR==10" file.txt
# Second

sed -n 10p file.txt
#Third

tail -n 10 file.txt | head -n 1
# Forth

head -n 10 file.txt | tail -n 1
# Fifth
