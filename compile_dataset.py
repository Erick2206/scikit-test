import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
import os


def getMovies():
    savePath='./Results/secondaryMovies.csv'
    movie_df=pd.DataFrame()
    if not os.path.isfile(savePath):
        movie_link='https://archive.ics.uci.edu/ml/machine-learning-databases/movies-mld/data/main.html'
        movie_html=requests.get(movie_link)
        soup= BeautifulSoup(movie_html.content, 'html.parser')


        tables = soup.find_all("table")
        for table in tables:
            rows=table.find_all("tr")

            for row in rows:
                data=row.find_all('td')
                try:
                    movie_list= data[0].find_all('td')
                    movie_df=movie_df.append({'movie_name': str(movie_list[0].contents[0])[3:]}, ignore_index=True)

                except:
                    continue

        movie_df=movie_df.drop_duplicates(subset="movie_name")
        movie_df.to_csv(savePath, sep=',', encoding='utf-8')

    else:
        movie_df=pd.read_csv(savePath)

    return movie_df


def loadPrimaryDataset():
    path='./Dataset/movies_metadata.csv'

    primaryDataset=pd.read_csv(path)

    return primaryDataset

def levenshteinDistance(primaryMovies,secondaryMovies):
    levDistDF=pd.DataFrame()
    count=0
    savePath='./Results/LevenshteinDistance.csv'
    if not os.path.isfile(savePath):
        for pindex,prow in primaryMovies.iterrows():
            if count==10:
                break

            for sindex,srow in secondaryMovies.iterrows():
                try:
                    levDist=fuzz.ratio(prow['title'],srow['movie_name'])

                except:
                    levDist=-1

                levDistDF=levDistDF.append({"Primary Movie":prow['title'], "Secondary Movie": srow['movie_name'], "Levenshtein Distance": levDist}, ignore_index=True)

            count+=1
            print "Done row", pindex

        levDistDF.to_csv(savePath, sep=',', encoding='utf-8', index=False)

    else:
        levDistDF=pd.read_csv(savePath)
    print levDistDF
    return levDistDF

if __name__=="__main__":
    secondaryMovies=getMovies()
    primaryMovies=loadPrimaryDataset()
    combinedLev=levenshteinDistance(primaryMovies,secondaryMovies)
#    combinedLev.to_csv('./Results/LevenshteinDistance.csv',ignore_index=True)
    print combinedLev.shape
    print "Done"
