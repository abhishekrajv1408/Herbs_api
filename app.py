from flask import Flask,request,jsonify
from diet_plan import herb
from adultration import Adulttration
import pandas as pd
import numpy as np

app=Flask(__name__)



@app.route("/",methods=['POST','GET'])
def herbs():
    data = request.get_json()
    sweet = int(data.get('sweet'))
    sour = int(data.get('sour'))
    pungent = int(data.get('pungent'))
    bitterness = int(data.get('bitterness'))
    option = int(data.get('option'))
    sweet = int(sweet/10)
    sour = int(sour/10)
    pungent = int(pungent/10)
    bitterness = int(bitterness/10)
    x_test = pd.DataFrame({
        "sweet":sweet,
        "sour":sour,
        "pungent":pungent,
        "bitterness":bitterness
    }, index = [0])
    if(option == 0):
        result = herb(x_test)
        data = np.array(["Not harmfull for human","Good for small baby", "Good for Adults", "Harmfull for Human body"])
        ans = data[result]
    elif(option == 1):
        result = Adulttration(x_test)
        ans = result.tolist()
        # ans = pd.DataFrame({"result":result })


    # result = result.tolist()
    
    return jsonify({"result":ans})

if __name__ == '__main__':
    app.run(debug=True)