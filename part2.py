# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019096         
# Date: 7/4/2021

#Part 2


#Creating Variables
cpass = 0
cdefer = 0
cfail = 0
total = 0
marks_list = [0, 20, 40, 60, 80, 100, 120]
loop = True
user_Error = True

#User Input
while loop == True:
    try:
        cpass = int(input("Enter your credits at pass: "))
        if cpass in marks_list:
            cdefer = int(input("Enter your credits at defer: "))
            if cdefer in marks_list:
                cfail = int(input("Enter your credits at fail: "))
                if cfail in marks_list:
                    loop = True
                    user_Error = False
                else:
                    print("Out of Range")
                    user_Error = True
            else:
                print("Out of Range")
                user_Error = True
        else:
            print("Out of Range")
            user_Error = True
    except:
        print("Integer required!")
    if user_Error == False:
        total = cpass + cdefer + cfail
        if total == 120:
            loop = False
            user_Error = False
        else:
            print("Total incorrect")
            user_Error = True
        

#Conditional Statements
if (cpass == 120) :
    print("┊ Progress ┊")
elif (cpass >= 100) :
    print("┊ Progress (module trailer) ┊")
elif (cfail >=80):
    print("┊ Exclude ┊")
else :
    print("┊ Do not progress – module retriever ┊")
    
