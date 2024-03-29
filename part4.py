# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019096         
# Date: 9/4/2021

#Part 4


#Creating Variables
tpass = 0
tdefer = 0
tfail = 0
total = 0
user_Opt = "y"
prog_Count = 0
trail_Count = 0
ex_Count = 0
ret_Count = 0
total_Outcomes = 0
marks_list = [0, 20, 40, 60, 80, 100, 120]

#Creating Functions
def star(a, b, c, d):
    while ((a != 0) or (b != 0) or (c != 0) or (d != 0)):
        if a > 0:
            print("\t*", end="\t")
            a = a - 1
        else:
            print("\t ", end="\t")
        if b > 0:
            print("*", end="\t")
            b = b - 1
        else:
            print(" ", end="\t")
        if c > 0:
            print("\t*", end="")
            c = c - 1
        else:
            print("\t ", end="")
        if d > 0:
            print("\t\t*")
            d = d - 1
        else:
            print("\t\t ")

#User Input
print("Staff Version with Histogram")
print(" \n")
while (user_Opt == "y"):
    user_Error = False
    loop = True
    while loop == True:
        try:
            tpass = int(input("Enter your credits at pass: "))
            if tpass in marks_list:
                tdefer = int(input("Enter your credits at defer: "))
                if tdefer in marks_list:
                    tfail = int(input("Enter your credits at fail: "))
                    if tfail in marks_list:
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
            user_Error = True
        if user_Error == False:
            total = tpass + tdefer + tfail
            if total == 120:
                loop = False
                user_Error = False
            else:
                print("Total incorrect")
                user_Error = True     
        
#Conditional Statements
    if (tpass == 120) :
        print("┊ Progress ┊")
        prog_Count = prog_Count + 1
    elif (tpass >= 100) :
        print("┊ Progress (module trailer) ┊")
        trail_Count = trail_Count + 1
    elif (tfail >=80):
        print("┊ Exclude ┊")
        ex_Count = ex_Count + 1
    else :
        print("┊ Do not progress – module retriever ┊")
        ret_Count = ret_Count + 1 

#Histogram
    print("  \n")
    print("Would you like to enter another set of data?")
    user_Opt = input("Enter 'y' for yes or 'q' to quit and view results: ")
    print("  \n")
    if (user_Opt == "q"):
        print("Vertical Histogram")
        print("Progress ", prog_Count, "|", "Trailer ", trail_Count, "|", "Retriever ", ret_Count, "|", "Exclude ", ex_Count)
        star(prog_Count, trail_Count, ret_Count, ex_Count)
        total_Outcomes = prog_Count + trail_Count + ex_Count + ret_Count
        print(total_Outcomes, " outcomes in total.")

