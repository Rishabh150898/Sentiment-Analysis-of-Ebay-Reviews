from flask import Flask,render_template, jsonify, request
#from sklearn.externals import joblib
import joblib
import nltk
import pickle

import flask
app = Flask(__name__)
save_cv = pickle.load(open('count-Vectorizer.pkl','rb'))
model = pickle.load(open('Ebay_Review_Classification.pkl','rb'))


def test_model(sentence):
    sen = save_cv.transform([sentence]).toarray()
    res = model.predict(sen)[0]
    if res == 'Positive':
        return 'Positive review'
        print("positive")
    elif res == 'Neutral':
        return 'Neutral review'
    else:
        return 'Negative review'
        print("Negative")


@app.route('/')
def index():
    return flask.render_template('int.html')


@app.route('/test_model', methods=['GET','POST'])
def abc():
    sent=request.form['Course']
    #data ='hi this product is good'


    res = test_model(sent)




    return render_template("int.html",result=res)


if __name__ == '__main__':
    app.run(debug=True)