from flask import Flask, render_template
import json 
from mypyfiles.jsonHandler import JSONHandler

app = Flask(__name__) 
JSON_DATA_HANDLE = JSONHandler()


@app.route("/")
def index(): 
    json_data = JSON_DATA_HANDLE.returnJSONDataFromJSONFile()
    print(json_data)


    


    

    return render_template("index.html")


if __name__ == "__main__": 
    app.run(debug=True) 



    
    