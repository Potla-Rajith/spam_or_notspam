# spam_or_notspam

## Data Acquisition
I acquired email dataset from Kaggle, which provided a collection of labeled emails indicating whether data is spam or not spam.

## Data Cleaning and Exploration
Using Jupyter Notebook, I performed initial data exploration to understand the structure and distribution of dataset. This involved:

Checking for missing values and handling them appropriately.

Analyzing the distribution of spam versus non-spam emails.

Visualizing common words and phrases in spam and non-spam emails.
## Text Preprocessing
I used NLTK (Natural Language Toolkit) for text preprocessing, which included:

Tokenization: Splitting emails into individual words.

Removing stopwords: Filtering out common words that do not contribute to the classification.

Lemmatization: Reducing words to their base forms.

Vectorization: Converting text data into numerical format using techniques like TF-IDF.

## Feature Selection
I evaluated different feature selection methods to identify the most relevant features for our model. This step helped in reducing the dimensionality of the dataset by removing irrelevant or redundant features.

## Model Selection and Training
I experimented with various machine learning algorithms using Scikit-learn to find the best-performing model. The algorithms tested included:

Logistic Regression

Support Vector Machines (SVM)

Naive Bayes

Random Forest

After evaluating the models based on performance metrics like accuracy, precision, recall, and F1-score, I selected Support Vector Machines (SVM) as the final model due to its superior performance.

## Saving the Model
I saved the trained SVM model and the vectorizer using Pickle to ensure compatibility with both dense and sparse matrix formats. This allowed me to easily load and use the model in our Streamlit application.

## Building the Streamlit Application
I developed a Streamlit web application to provide an interactive interface for users to input email text and receive predictions. The steps involved were:

Creating an input box for users to enter email text.

Loading the pre-trained SVM model and vectorizer.

Processing the input text and making predictions.

Displaying the prediction result (spam or not spam) on the web interface.

## Testing and Deployment
I thoroughly tested the Streamlit application to ensure it worked correctly and provided accurate predictions. Once satisfied with the performance, I deployed the application for users to access.

## Documentation
Finally, I documented the entire process, including installation instructions, usage guide, and project overview, to make it easier for others to understand and use email spam classifier.
