import requests
import json

# we take the api  to take data from saral webside using request module

saral_api = "http://saral.navgurukul.org/api/courses"
saral_url = requests.get(saral_api)
data = saral_url.json()
# we creat a json file to store a data as a saral data
with open("courses.json","w") as saral_data :
    json.dump(data,saral_data,indent=4)

# we want the courses to select among them

serial_no = 1
for courses in data["availableCourses"]:
    print(serial_no ,".",courses["name"],courses["id"])
    serial_no += 1
course = int(input("enter the course number: "))
print(data["availableCourses"][course-1]["name"])

# If we want to go back and choose courses which we want and confirm it 

user_input1=input("Do you want to previous or next: ")
if user_input1 == "previous" :
    serial_no = 1
    for courses in data["availableCourses"]:
        print(serial_no ,".",courses["name"],courses["id"])
        serial_no += 1
       
            
    course = int(input("enter the course number: "))
    print(data["availableCourses"][course-1]["name"])  

# Here we dicplay which topic included in courses . Display the topic of the courese

saral_api__1 = ("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][course-1]["id"])+"/exercises")
saral_url_1=requests.get(saral_api__1)
data_1 = saral_url_1.json()
with open ("parents.json","w") as saral_data_1 :
    json.dump(data_1,saral_data_1,indent=4)      
        
#childExercises 
#name
no=0
List=[]
for child in range(len(data_1["data"])):
    no+=1
    print("        ",no,".",data_1["data"][child]["name"])
    serial_no_1=1
    if data_1["data"][child]["childExercises"] == List:
        print("             ",serial_no_1,".",data_1["data"][child]["slug"])
        serial_no_1 += 1
    else:
        #question
        serial_no=1
        for Question in range(len(data_1["data"][child]["childExercises"])):
            print("              ",serial_no,".",data_1["data"][child]["childExercises"][Question]["name"])
            serial_no+=1
Slug= int(input("Enter the number of slug :"))
print(data_1["data"][Slug-1]["name"])
#Previous or next
number1=input("Do you want to previous or next: ")
if number1 == "previous":
    no=0
    List=[]
    for child in range(len(data_1["data"])):
        no+=1
        print("        ",no,".",data_1["data"][child]["name"])
        serial_no_1=1
        if data_1["data"][child]["childExercises"] == List:
            print("             ",serial_no_1,".",data_1["data"][child]["slug"])
            serial_no_1 += 1
        else:
            #question
            serial_no=1
            for Question in range(len(data_1["data"][child]["childExercises"])):
                print("              ",serial_no,".",data_1["data"][child]["childExercises"][Question]["name"])
                serial_no+=1
    Slug= int(input("Enter the number of slug :"))
    print(data_1["data"][Slug-1]["name"])
    serial_no=1
    for Question in range(len(data_1["data"][Slug-1]["childExercises"])):
        if data_1["data"][child]["childExercises"] == List:
            print("              ",serial_no,".",data_1["data"][Slug-1]["childExercises"][Question]["name"])
            serial_no+=1
else:
    slug_ind=[]

    no=0
    List=[]
    for child in range(len(data_1["data"])):
        no+=1
        serial_no_1=1
        if data_1["data"][child]["childExercises"] == List:
            serial_no_1 += 1
    
            serial_no=1
            for Question in range(len(data_1["data"][Slug-1]["childExercises"])):
                if data_1["data"][child]["childExercises"] == List:
                    print("              ",serial_no,".",data_1["data"][Slug-1]["childExercises"][Question]["name"])
                    slug = data_1["data"][Slug-1]["childExercises"][Question]["slug"]
                    parent = data_1["data"][Slug-1]["childExercises"][Question]['id']
                    slug1 = requests.get(link)
                    slug2 = slug1.json()
                    slug_ind.append(slug2["content"])
                    serial_no+=1
            break
question_1 = int(input("Enter the question  number: "))
question=question_1-1
print(slug_ind[question])
while question_1 > 0:
    next_question = input("Do you want next or previous: ")
    if question_1 == len(slug_ind):
         print("next page")
    if next_question == "previous":
        if  question_1 == 1:
            print("no more question")
            break
        elif question_1 > 0:
            question_1 = question_1 - 2
            print(slug_ind[question_1])
    elif next_question == "next":
        if  question_1 < len(slug_ind):
            index = question_1 + 1
            print(slug_ind[index-1])
            question += 1
            question_1 = question_1 + 1
            if question == (len(slug_ind)-1):
                print("next page")
                break