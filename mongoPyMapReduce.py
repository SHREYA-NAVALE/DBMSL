from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Mock']
collection = db['Integration']

def insertBook():
    name = input("Enter Name Of the BOOK")
    pages = int(input("Enter Total Number of Pages"));
    book = {"name" : name , "pages" : pages , "type": "Big Book" if pages > 500 else "Small Book"}
    collection.insert_one(book)

    

def displayBooks():
    for book in collection.find():
        print(book)


def mapReduce():
    map_function = """
    function() {
        emit(this.type, 1);  
    }
    """
    reduce_function = """
    function(key, values) {
        return Array.sum(values);  // Sum the 1s for each category
    }
    """
    
    db.command(
        'mapReduce',
        'Integration',  
        map=map_function,
        reduce=reduce_function,
        out="Result"
    )
    
    for rec in db["Result"].find():
        print(rec)

def menu():
    while True:
        print("Python Mongo Connectivity")
        print("Select Operation to be performend...")
        print("1.Insert Book")
        print("2.Display Books")
        print("3.MapReduce")
        print("4.Exit")

        choice = int(input("Enter Your Choice"))

        if choice == 1:
            insertBook()
        elif choice == 2:
            displayBooks()
        elif choice == 3:
            mapReduce()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("INvalid Input")
    

if __name__ == "__main__":
    menu()

    client.close()
