import pickle
from flask import Flask,request

api=Flask(__name__)

with open('ai.pkl','rb') as f:
    ai=pickle.load(f)

@api.route('/')
def home():
    return "API Server Running"

@api.route('/predict',methods=['GET'])
def predict():
    ID=request.args.get('ID')
    ID=float(ID)
    data=[[ID]]
    response=ai.predict(data)[0]
    return response

if __name__=="__main__":
        api.run(
            host='0.0.0.0',
            port=2000
        )
