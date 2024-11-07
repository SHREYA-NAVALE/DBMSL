from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Mock']
collection = db['Student']

def insert():
    roll = int(input("Enter Roll Number : "))
    name = input("Enter Name : ")
    sem = int(input("Enter Semester : "))
    year = int(input("Enter Year : "))
    backlogs = int(input("Enter Total Number of Backlogs : "))

    data = {
        "roll" : roll,
        "name" : name,
        "sem" : sem,
        "year" : year,
        "backlogs" : backlogs
    }

    collection.insert_one(data)

def display():
    for record in collection.find():
        print(record)

def delete():
    collection.delete_many({"backlogs" : {"$gt" : 4}})

def retrive():
    rollno = int(input("Enter Roll Number To be Retrived"))
    result = collection.find({"roll" : rollno})

    for r in result:
        print(r)
# insert()
# display()
# delete()
display()
retrive()