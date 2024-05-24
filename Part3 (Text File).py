#part 3
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

#using a while loop to execute a block of code repeatedly until the condition is true
while True :
    
    #using try except to catch errors
    try:
    
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
        
    elif pass_credits==100:
        print("Progress (module trailer)\n")
        Trailer_count+=1
        list_of_trailer.append([pass_credits,defer_credits,fail_credits])
        
    elif ((pass_credits<=40) and (defer_credits<=40) and (fail_credits>=80)):
        print("Exclude \n")
        Exclude_count+=1
        list_of_exclude.append([pass_credits,defer_credits,fail_credits])
        
    else:
        print("Module retriever \n")
        Retriever_count+=1
        list_of_retriever.append([pass_credits,defer_credits,fail_credits])
        
    #the appropriate progression for each student untill the staff member enters 'b'(break) to exit can also optionally allow you to 'y'(continue) to proceed    
    answer=input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
    print("\n")
    if answer.lower()=='q':
        break
    else:
        continue
   
# calculating the progress,trailer,retriever and exclude count total (The total number of students)
Total_count=Progress_count+Trailer_count+Retriever_count+Exclude_count

print("---------------------------------------------------------------------------")
#display the number of students for each progression category(histogram)
print("Histogram")
print("Progress",Progress_count," :" + "*"*Progress_count)
print("Trailer",Trailer_count,"  :" + "*"*Trailer_count)
print("Retriever",Retriever_count,":" + "*"*Retriever_count)
print("Exclude",Exclude_count,"  :" + "*"*Exclude_count)
print("\n")

#print the total number of students
print(Total_count,"outcomes in total. \n")

print("----------------------------------------------------------------------------")
#printing the data stored in the list(using for loop)
print("Part 2 :")
for credits in list_of_progress:
    print(f"Progress -{','.join(str(i) for i in credits)} ")
for credits in list_of_trailer:
    print(f"Progress (module trailer) - {','.join(str(i) for i in credits)}")
for credits in list_of_exclude:
    print(f"Exclude - {','.join(str(i) for i in credits)}")
for credits in list_of_retriever:
    print(f"Module retriever - {','.join(str(i) for i in credits)}")


#open new text file (read and write)-w/r/a
with open("credits.txt","w") as file:

# Save progression data to text file (write)

    file.write("Part 3 :\n")
    for credits in list_of_progress:
        file.write(f"Progress -{','.join(str(i) for i in credits)}\n ")
    for credits in list_of_trailer:
        file.write(f"Progress (module trailer) - {','.join(str(i) for i in credits)}\n")
    for credits in list_of_exclude:
        file.write(f"Exclude - {','.join(str(i) for i in credits)}\n")
    for credits in list_of_retriever:
        file.write(f"Module retriever - {','.join(str(i) for i in credits)}\n")

