import pymongo

def Test_Mongo():

  client = pymongo.MongoClient('mongodb://143.244.190.214', 27018,
  username="admin",
  password="pass")

  dbnames = client.list_database_names()
  if 'creditcards' in dbnames:
    print("It's there!")
    mydb = client["creditcards"]
    mycol = mydb["inventory"]

    mytest = { "Credit Card" : "TEST1234" }

    y = mycol.insert_one(mytest)

    for x in mycol.find():
      print(x)

  else:
    print("Noup, not here...")
    mydb = client["creditcards"]
    mycol = mydb["inventory"]
    mytest = { "Credit Card" : "TEST1234" }

    y = mycol.insert_one(mytest)
    
    print("DB created")


if __name__ == "__main__":
  Test_Mongo()