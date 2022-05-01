from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

app = Flask(__name__)

@app.route('/')
def WebNew():
   return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
	df= pd.read_csv("bbc-text.csv", encoding="latin-1")
	
	# # # Features and Labels
	df['label'] = df['category'].map({'politics': 0, 'sport': 1,'entertainment':2,'tech':3,'international':4})
	X = df['text']
	y = df['label']
	my_prediction = "Accuracy"
	# # # Extract Feature With CountVectorizer
	cv = CountVectorizer()
	X = cv.fit_transform(X) # Fit the Data
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.18, random_state=42)
	# # #Naive Bayes Classifier
	from sklearn.naive_bayes import MultinomialNB

	clf = MultinomialNB()
	clf.fit(X_train,y_train)
	clf.score(X_test,y_test)
	

	if request.method == 'POST':
		      message = request.form['message']
		      data = [message]
		      vect = cv.transform(data).toarray()
		      my_prediction = clf.predict(vect)
                        
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)
