# BBC-News-classification using different algorithms

1. Dataset Preparation: The first step is the Dataset Preparation step which includes the process of loading a dataset and performing basic pre-processing. 

    •	Mount the google drive to use the file from drive.

    •	Load the BBC News dataset which can be downloaded from Kaggle.

    •	Download dataset: https://www.kaggle.com/datasets/yufengdev/bbc-fulltext-and-category

    •	Read the data, we can see categories v/s Text(article headline text).

    •	Remove unnecessary columns.

    •	Count unique categories & text for each.

    •	Visualize the count of articles for each category.

    •	Remove duplicate rows.

    •	Find word cloud, most frequent words from ‘text’ column.

    •	Pre-processing & Tokenization is performed in this step mainly.
  

2. Feature Engineering: The next step is the Feature Engineering in which the raw dataset is transformed into flat features which can be used in a machine learning model. This step also includes the process of creating new features from the existing data. The dataset is then spitted into train and validation sets.
      •	Main step is converting text into suitable features.

      •	Count Vectors as features.

      •	TF-IDF Vectors as features.

      •	Split the dataset into Train & Test datasets.

3. Model Training: The final step is the Model Building step in which a machine learning model is trained on a labelled dataset.

      •	Train the model using different algorithms:
      1.	Naive Bayes Classifier
      2.	Logistic Regression
      3.	Decision Tree Classifier
      4.	Linear Support Vector Machine (Linear SVC)
      5.	Random Forest Classifier

      •	Get the accuracy and predict a test sample to know which category the text belongs to.

      •	It will predict the ‘category’ of article text.

      •	Compare the accuracy of models.
  
  4. Improve Performance of Text Classifier: In this article, we will also look at the different ways to improve the performance of text classifiers.

      •	Text cleaning.

      •	NLP features with text feature vectors.

      •	Using exhaustive stop word list.

Web app using Flask

1.	Main : App.py 
This file contains main code needed to run an application.
2.	dev: All the dependency files are listed.
3.	templates: This folder contain html pages, User Interface code which is appeared on front-end pages.
4.	static: This folder contains css required for front end page.
5.	NB_bbc_news.pkl : This is downloaded from the saved model.

      •	We ran our application as a single module; thus we initialized a new Flask instance with the argument __name__ to let Flask know that it can find the HTML template.
     folder (templates) in the same directory where it is located.

      •	Next, we used the route decorator (@app.route('/')) to specify the URL that should trigger the execution of the home function.

      •	Our home function simply rendered the home.html HTML file, which is located in the templates folder.

      •	Inside the predict function, we access the BBC news data set, pre-process the text, and make predictions, then store the model. We access the new article text entered by the user and use our model to make a prediction for its label.

      •	we used the POST method to transport the form data to the server in the message body. Finally, by setting the debug=True argument inside the app.run method, we further activated Flask's debugger.

      •	Lastly, we used the run function to only run the application on the server when this script is directly executed by the Python interpreter, which we ensured using the if statement with __name__ == '__main__'.


