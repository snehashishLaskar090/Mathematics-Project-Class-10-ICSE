from flask import *
from Commercialathematics import *

app = Flask(__name__)

@app.route('/si', methods= ["GET", "POST"])
def si():

    if request.method == "GET":
        pass

@app.route('/simain', methods = ["GET", "POST"])

def main():

    if request.method == "POST":

        principle = int(request.form.get("principle"))
        rate = int(request.form.get("rate"))
        time = int(request.form.get("time"))
        
        result = SimpleInterest(principle=principle, rate=rate, time=time)
        return render_template("simpleinterest.html",interest = result) 


    else:

        return render_template("simpleinterest.html",interest = True) 

if __name__ == "__main__":
    app.run(debug=True)