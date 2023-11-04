from flask import Flask, request, jsonify
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

load_model = pickle.load(open('model_predic_lr.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify("Hello 66666")

@app.route('/predict', methods=['POST'])
def predict():

    try:
        #รับข้อความที่เป็นภาษาอังกฤษ
        data = request.get_json()['message']

        prediction = load_model.predict([data]) #รับมาใส่ในโมเดล จะได้ค่า 0,1

        if prediction[0] == 0:
            result = "Hammmmmm"
        elif prediction[0] == 1:
            result = "Spammmmm"

        return jsonify({'result': result})  # ส่งข้อมูลเป็น JSON
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
