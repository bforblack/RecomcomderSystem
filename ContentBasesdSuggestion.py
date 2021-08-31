import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
from DataExtracter import FetchMovieData
from ast import literal_eval
import numpy as np


class ContentBasesdSuggestion:
    def __init__(self):
        logging.info("--------Content Based Suggestions---------")


    def generateContentBasesSuggestion(self,data,movieName):
        tdif=TfidfVectorizer(stop_words='english')
        tdifmetrices=tdif.fit_transform(data['overview'].fillna(''))
        cosin_similarity=linear_kernel(tdifmetrices,tdifmetrices)
        dataIndex=pd.Series(data.index,index=data.title)
        index=dataIndex[movieName]
        prediction=sorted(list(enumerate(cosin_similarity[index])),reverse=True)
        final_list=prediction[1:10]
        movieList=[]
        for li in final_list:
            movieList.append(data.title[li[0]])
        print(movieList)
        columnList=['cast','crew','genres','keywords','production_companies']
        for field in columnList :
            data[field]=data[field].apply(literal_eval)
        data['director']=data['crew'].apply(self.fetch_director_data)


    def fetch_director_data(self,actor_data):
        for j in actor_data:
                if j['job'] == 'Director':
                    return j['name']

        return np.nan













if __name__ == '__main__':
    ContentBasesdSuggestion().generateContentBasesSuggestion(FetchMovieData().generateData(),"Avatar")



