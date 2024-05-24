#Part 1 (D)
#represents a student who has achieved a progress result within each progress range.start to count 0
Progress_count=0
Trailer_count=0
Retriever_count=0
Exclude_count=0

# define the function
def search_error(value):
    
    #using try except to catch errors
    try:
        value = int(value)
        if value not in range (0,121,20):
            print("Out of range \n")
            return "error"
        return value
    
    except ValueError:
        print("Integer required \n")
        return "error"


#using a while loop to execute a block of code repeatedly until the condition is true
while True:

    # To loop until a valid input is given
    while True:
            #Obtaining the pass credit count
            pass_credits = input("Enter the number of credits at pass: ")
            pass_credits =  search_error(pass_credits)
            if pass_credits != "error":
                break

    while True:
            #Obtaining the defer credit count
            defer_credits = input("Enter the number of credits at defer: ")
            defer_credits = search_error(defer_credits)
            if defer_credits != "error":
                break

    while True:
            #Obtaining the fail credit count
            fail_credits = input("Enter the number of credits at fail: ")
            fail_credits = search_error(fail_credits)
            if fail_credits != "error":
                break
            
 #calculating the credits of total
    total= pass_credits+defer_credits+fail_credits
    
    #determine the progression outcome
    if total !=120:
        print("Total incorrect \n")
        
    elif pass_credits==120:
        print("Progress \n")
        Progress_count+=1
        
    elif pass_credits==100:
        print("Progress (module trailer) \n")
        Trailer_count+=1
        
    elif ((pass_credits<=40) and (defer_credits<=40) and (fail_credits>=80)):
        print("Exclude \n")
        Exclude_count+=1
        
    else:
        print("Module retriever \n")
        Retriever_count+=1

    #the appropriate progression for each student untill the staff member enters 'b'(break) to exit can also optionally allow you to 'y'(continue) to proceed
    answer=input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
    print("\n")
    if answer.lower()=='q':
         break
    else :
        continue
    
# calculating the progress,trailer,retriever and exclude count total (The total number of students)
Total_count=Progress_count+Trailer_count+Retriever_count+Exclude_count

print("--------------------------------------------------------------------------------------------------------------------------")
#display the number of students for each progression category
print("Histogram")
print("Progress",Progress_count," :" + "*"*Progress_count)
print("Trailer",Trailer_count,"  :" + "*"*Trailer_count)
print("Retriever",Retriever_count,":" + "*"*Retriever_count)
print("Exclude",Exclude_count,"  :" + "*"*Exclude_count)
print("\n")

#print the total number of students
print(Total_count,"outcomes in total.")


