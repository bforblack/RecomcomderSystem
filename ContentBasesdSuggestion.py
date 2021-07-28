import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
from DataExtracter import FetchMovieData


class ContentBasesdSuggestion:
    def __init__(self):
        logging.info("--------Content Based Suggestions---------")


    def generateContentBasesSuggestion(self,data,movieName):
        tdif=TfidfVectorizer(stop_words='english')
        tdifmetrices=tdif.fit_transform(data['overview'].fillna(''))
        cosin_similarity=linear_kernel(tdifmetrices,tdifmetrices)
        dataIndex=pd.Series(data.index,index=data.title)
        index=dataIndex[movieName]
        prediction=cosin_similarity[index]



if __name__ == '__main__':
    ContentBasesdSuggestion().generateContentBasesSuggestion(FetchMovieData().generateData(),"Avatar")



