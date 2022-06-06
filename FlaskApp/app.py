from cgi import test
from unicodedata import name
from flask import Flask, render_template, url_for, request, jsonify
import pymongo

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/result',methods=['POST', 'GET'])
def result():

    #Conexion a Base de Datos
    client = pymongo.MongoClient('mongodb://143.244.190.214', 27018,
    username='admin',
    password='pass')
    dbnames = client.list_database_names()

    #Si queremos imprimir todas las DBs
    #print("DB Names: " + dbnames)

    output = request.form.to_dict()
    print(output)
    name = output["name"]

    nDigits = len(name)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(name[i]) - ord('0')

        print("Our D current value is: " +  str(d))

        print("Now, we convert the character into unicode:")
        print(str(d) + "\n")

        if (isSecond == True):
            d = d * 2
            print("Our D(2) current value is: " +  str(d))

  
        nSum += d // 10
        print("nSum1: " + str(nSum))
        nSum += d % 10
        print("nSum2: " + str(nSum))
  
        isSecond = not isSecond

    if (nSum % 10 == 0):
        print("Valid CC")
        #Insert dentro de la DB
        mydb = client["creditcards"]
        mycol = mydb["inventory"]

        mycc = { "Credit Card" : name }

        #La parte nueva del codigo es esta

        y = mycol.insert_one(mycc)
        print("El ID de la CC ingresada fue: " + str(y.inserted_id))

        last_cc = mycol.find_one({"_id" : y.inserted_id}, {"_id" : 0, "Credit Card" : 1})

        print("La CC ingresada es: " + str(last_cc))
        #La parte nueva del codigo es esta

        name = "valid"

    else:
        print("Invalid CC")
        name = "invalid"

    return jsonify({'status': 'ok', 'message': 'pong', 'reponse': '200', 'cc' : last_cc})
    #return render_template('index.html', name = name, lastcc = lastcc)

#Valid card: "79927398713"
    
if __name__ == "__main__":
    app.run(debug=True)