# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019096         
# Date: 7/4/2021

#Part 1


#Creating Variables
cpass = 0
cdefer = 0
cfail = 0

#User Input
cpass = int(input("Enter your credits at pass: "))
cdefer = int(input("Enter your credits at defer: "))
cfail = int(input("Enter your credits at fail: "))

#Conditional Statements
if (cpass == 120) :
    print("┊ Progress ┊")
elif (cpass >= 100) :
    print("┊ Progress (module trailer) ┊")
elif (cfail >=80):
    print("┊ Exclude ┊")
else :
    print("┊ Do not progress – module retriever ┊")

