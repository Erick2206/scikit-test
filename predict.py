import os
import numpy as np
import pandas as pd
from sklearn.svm import LinearSVR
from sklearn.linear_model import LassoLars
from ast import literal_eval
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelBinarizer



def load_dataset():
    savePath='./Dataset/movies_metadata.csv'
    data=pd.read_csv(savePath)
    data=data.drop(['belongs_to_collection','title','spoken_languages','production_countries','budget','homepage','id','imdb_id','overview','poster_path','release_date','runtime','tagline','status','original_title','video'],axis=1)
    return data

def preprocess(data):

    def cleanProductionComp(x):
        try:
            return literal_eval(x)[0]['name']

        except:
            return 'unknown'

    def cleanGenre(x):
        try:
            return literal_eval(x)[0]['name']

        except :
            return 'unknown'


    data=data[data.revenue != 0]
    data[pd.to_numeric(data.revenue, errors='coerce').notnull()]

    data['production_companies']=data['production_companies'].apply(cleanProductionComp)
    data['genres']=data['genres'].apply(cleanGenre)

    data.adult = pd.to_numeric(data.adult, errors='coerce').fillna(0).astype(np.int64)
    data.popularity = data.popularity.astype(float).fillna(0.0).astype(np.int64)
    data.vote_average=  data.vote_average.astype(float).fillna(0.0).astype(np.int64)
    data.vote_count = data.vote_count.astype(float).fillna(0.0).astype(np.int64)

    lb = LabelBinarizer()
    data['Genres Encoded']=lb.fit_transform(data['genres']).tolist()
    data['production_companies']=lb.fit_transform(data['production_companies']).tolist()
    data['original_language']=lb.fit_transform(data['original_language']).tolist()
    data['adult']=lb.fit_transform(data['adult']).tolist()

    x_cols=['Genres Encoded','original_language','popularity','production_companies','vote_average','vote_count']
    y_cols=['revenue']

#    data['Genres Encoded'].to_csv('temp.csv')
    return data[x_cols],data[y_cols]

def dataSplit(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def SVMRegression(X_train, X_test, y_train, y_test):
    regr = LinearSVR(random_state=0)
    regr.fit(X_train,y_train)
    predictions=regr.predict(X_test)
    return predictions

def LassoRegression(X_train, X_test, y_train, y_test):
    regr=LassoLars(alpha=0.1)
    print len(X_train.values.tolist()[0])
    print len(X_train.values.tolist())
    regr.fit(X_train.values.tolist(),y_train.values.tolist())
    predictions=regr.predict(X_test)
    return predictions

def getScores(predicted,actual):
    return mean_squared_error(actual,predicted)

if __name__=="__main__":
    data=load_dataset()
    X,y=preprocess(data)
    X_train, X_test, y_train, y_test=dataSplit(X,y)
#    print X_train.head()
#    SvmPredictions=SVMRegression(X_train, X_test, y_train, y_test)
#    LassoPredictions=LassoRegression(X_train, X_test, y_train, y_test)

#    SvmScore=getScores(SvmPredictions,y_test)
#    LassoScore=getScores(LassoPredictions,y_test)

#    print "SVM Score is ",SvmScore
#    print "Lasso Score is ",LassoScore
