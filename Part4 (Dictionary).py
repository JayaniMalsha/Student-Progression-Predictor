
#represents a student who has achieved a progress result within each progress range.start to count 0
Progress_count=0
Trailer_count=0
Retriever_count=0
Exclude_count=0

#create list
list_of_progress=[]
list_of_trailer=[]
list_of_retriever=[]
list_of_exclude=[]

#create dictionary
dictionary={}

#using a while loop to execute a block of code repeatedly until the condition is true    
while True :
    
        #using try except to catch errors
        try:
            #Obtaining the student id
            student_id = input("Enter the student id : ")
            if student_id not in ["w1234567" ,"w1234566" ,"w1234565" ,"w1234564" ,"w1234563"]:
                print("Enter the valid student_id")
                continue
            #Obtaining the pass credit count
            pass_credits = int(input("Enter the number of credits at pass: "))
            #also looking out of range
            if pass_credits not in range (0,121,20):
                print("Out of range \n")
                continue
            
            #Obtaining the defer credit count
            defer_credits = int(input("Enter the number of credits at defer: "))
            if defer_credits not in range (0,121,20):
                print("Out of range \n")
                continue
            
            #Obtaining the fail credit count
            fail_credits = int(input("Enter the number of credits at fail: "))
            if fail_credits not in range (0,121,20):
                print("Out of range \n")
                continue
            
        except ValueError:
            #cheking if integer required
            print("Integer required \n")
            continue

        #calculating the credits of total
        total= pass_credits+defer_credits+fail_credits

        #determine the progression outcome
        if total !=120:
            print("Total incorrect \n")
            
            
        elif pass_credits==120:
            print("Progress \n")
            Progress_count+=1
            #storing data(credit counts) in list (progression category)
            list_of_progress.append([pass_credits,defer_credits,fail_credits])
            #storing the input progress data in a dictionary
            dictionary[student_id]=f"progress - {pass_credits},{defer_credits},{fail_credits}"
            
        elif pass_credits==100:
            print("Progress (module trailer) \n")
            Trailer_count+=1
            list_of_trailer.append([pass_credits,defer_credits,fail_credits])
            dictionary[student_id]=f"Progress (module trailer) - {pass_credits},{defer_credits},{fail_credits}"
            
        elif ((pass_credits<=40) and (defer_credits<=40) and (fail_credits>=80)):
            print("Exclude \n")
            Exclude_count+=1
            list_of_exclude.append([pass_credits,defer_credits,fail_credits])
            dictionary[student_id]=f"Exclude - {pass_credits},{defer_credits},{fail_credits}"
            
        else:
            print("Module retriever \n")
            Retriever_count+=1
            list_of_retriever.append([pass_credits,defer_credits,fail_credits])
            dictionary[student_id]=f"Module retriever - {pass_credits},{defer_credits},{fail_credits}"
            
        #the appropriate progression for each student untill the staff member enters 'b'(break) to exit can also optionally allow you to 'y'(continue) to proceed    
        answer=input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        print("\n")

        if answer.lower()=='q':
            break
        else :
            continue

#part 4
print("---------------------------------------------------------------------")        
print("Part 4 : ")
#solution add student IDs as part of input and display with results(x=key,y=value)
for x,y in dictionary.items():
    print(f"{x} : {y}", end=" ")
print()
