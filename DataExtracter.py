import pandas as pd
import numpy as nm
import logging
class FetchMovieData:

    def generateData(self):
        data=pd.read_csv('C:/Users/Shivankur Tripathi/Downloads/archive/tmdb_5000_credits.csv')
        data2=pd.read_csv("C:/Users/Shivankur Tripathi/Downloads/archive/tmdb_5000_movies.csv")
        logging.info("Data Read")
        finaldata=pd.merge(data,data2)
        logging.info("Shape",finaldata.shape)
        return finaldata

if __name__ == '__main__':
    FetchMovieData().generateData()
