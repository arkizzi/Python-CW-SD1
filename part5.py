# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: 2019096         
# Date: 9/4/2021

#Part 5


#Creating Variables
tpass = 0
tdefer = 0
tfail = 0
total = 0
extracter = 0
prog_Count = 0
trail_Count = 0
ex_Count = 0
ret_Count = 0
total_Outcomes = 0

#Lists
values_List = [(120,0,0), (100,20,0), (100,0,20), (80,20,20), (60,40,20), (40,40,40), (20,40,60), (20,20,80), (20,0,100), (0,0,120)]


#Creating Functions
def hist(count):
    for i in range(0,count): 
       print("*", end="")
    

#List Process
for extracter in values_List:
    tpass, tdefer, tfail = extracter 
        
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
print("Horizontal Histogram")
print("Progress ", prog_Count, " :", end=" ")
hist(prog_Count)
print(" ")
print("Trailer  ", trail_Count, " :", end=" ")
hist(trail_Count)
print(" ")
print("Retriever", ret_Count, " :", end=" ")
hist(ret_Count)
print(" ")
print("Exclude  ", ex_Count, " :", end=" ")
hist(ex_Count)
print(" ")
total_Outcomes = prog_Count + trail_Count + ex_Count + ret_Count
print(total_Outcomes, " outcomes in total.")

