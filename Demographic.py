from DataExtracter import FetchMovieData
import logging
import pandas as pd

class Demographic:


    def __init__(self):
        logging.info("-----------Demographic Recomndation------")


    def demographicModel(self,data):
        data.shape
        logging.info("------------Data Provided with shape------",data.shape)
        c=data['vote_average'].mean()
        m=data['vote_count'].quantile(0.9)
        data2=data.loc[data.vote_count >=m]
        logging.info("Check")
        data2['scores']=self.demographicFormula(m,c,data2)
        data2=pd.DataFrame(data2).sort_values("scores",ascending=False)
        print(data2[['title', 'vote_count', 'vote_average', 'scores']].head(10))


    def demographicFormula(self,m,c,data):
        v=data['vote_count']
        r=data['vote_average']
        return (v/(v+m)*r) + (m/(v+m)*c)




if __name__ == '__main__':
    #data=
    prediction= Demographic().demographicModel(pd.DataFrame(FetchMovieData().generateData()))