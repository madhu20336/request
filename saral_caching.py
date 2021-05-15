import requests
import json
import os

# we take the api  to take data from saral webside using request module
if os.path.isfile("courses.json"):
    with open("courses.json","r") as saral_data :
        text_data = json.load(saral_data)
else:
    saral_api = "http://saral.navgurukul.org/api/courses"
    saral_url = requests.get(saral_api)
    data = saral_url.json()
    # we creat a json file to store a data as a saral data
    with open("courses.json","w") as saral_data :
        text_data = json.dump(data,saral_data,indent=4)

# we want the courses to select among them

serial_no = 1
for courses in text_data["availableCourses"]:
    print(serial_no ,".",courses["name"],courses["id"])
    serial_no += 1
course = int(input("enter the course number: "))
print(text_data["availableCourses"][course-1]["name"])

# If we want to go back and choose courses which we want and confirm it 

user_input1=input("Do you want to previous or next: ")
if user_input1 == "previous" :
    serial_no = 1
    for courses in text_data["availableCourses"]:
        print(serial_no ,".",courses["name"],courses["id"])
        serial_no += 1
    
            
    course = int(input("enter the course number: "))
    print(data["availableCourses"][course-1]["name"])  

# Here we dicplay which topic included in courses . Display the topic of the courese
if os.path.isfile("parent/" + text_data["availableCourses"][course-1]["name"]):
    with open ("parent/" + text_data["availableCourses"][course-1]["name"]+".json","r") as saral_data_1 :
        text_data1 = json.load(saral_data_1)
else:
    saral_api__1 = ("http://saral.navgurukul.org/api/courses/"+str(text_data["availableCourses"][course-1]["id"])+"/exercises")
    saral_url_1=requests.get(saral_api__1)
    text_data1 = saral_url_1.json()
    with open ("parent/" + text_data["availableCourses"][course-1]["name"] + ".json" ,"w") as saral_data_1 :
        data1 = json.dump(text_data1,saral_data_1,indent=4)  
        
# print(text_data1)   
#childExercises 
#name
no=0
List=[]
for child in range(len(text_data1["data"])):
    no+=1
    print("        ",no,".",text_data1["data"][child]["name"])
    serial_no_1=1
    if text_data1["data"][child]["childExercises"] == List:
        print("             ",serial_no_1,".",text_data1["data"][child]["slug"])
        serial_no_1 += 1
    else:
        # print("        ",serial_no,".",data_1["data"][child]["childExercises"])
        #question
        serial_no=1
        for Question in range(len(text_data1["data"][child]["childExercises"])):
            print("              ",serial_no,".",text_data1["data"][child]["childExercises"][Question]["name"])
            serial_no+=1
        # /break    

Slug= int(input("Enter the number of slug :"))
print(text_data1["data"][Slug-1]["name"])
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
            # print("        ",serial_no,".",data_1["data"][child]["childExercises"])
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
            # print("             ",serial_no_1,".",data_1["data"][child]["slug"])
            print("              ",serial_no,".",data_1["data"][Slug-1]["childExercises"][Question]["name"])
            serial_no+=1
else:
    slug_ind=[]

    no=0
    List=[]
    for child in range(len(text_data1["data"])):
        no+=1
        # print("        ",no,".",data_1["data"][child]["name"])
        serial_no_1=1
        if text_data1["data"][child]["childExercises"] == List:
            # print("             ",serial_no_1,".",data_1["data"][child]["slug"])
            serial_no_1 += 1
    
            serial_no=1
            for Question in range(len(text_data1["data"][Slug-1]["childExercises"])):
                if text_data1["data"][child]["childExercises"] == List:
                    # print("             ",serial_no_1,".",data_1["data"][child]["slug"])
                    print("              ",serial_no,".",text_data1["data"][Slug-1]["childExercises"][Question]["name"])
                    slug = text_data1["data"][Slug-1]["childExercises"][Question]["slug"]
                    # print(parent)
                parent = text_data1["data"][Slug-1]["childExercises"][Question]['id']
                    # print(slug)
                    link = "http://saral.navgurukul.org/api/courses/"+parent+"/exercise/getBySlug?slug="+slug
                    slug1 = requests.get(link)
                    slug2 = slug1.json()
                    slug_ind.append(slug2["content"])
                    serial_no+=1
            break
# print(slug_ind)

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