
# my_lambdata/class3.py
​
import pandas
from datetime import datetime
# GOAL: refactor from a functional approach to OOP approach
# could make a State class
# could create a class for Abbreviations
# could have the data frame a attribute of the class instance,
# ... have the existing function a method of the class.
​
​
class DataTransformer():
    def __init__(self, my_df):
        """
        Params my_df (pandas.DataFrame) with with column called "abbrev" which has state abbrevs
        """
        self.df = my_df.copy()
​
    def another_example(self):
        print("WE'RE DOING ANOTHER THING")
        self.convert_names()
​
    def convert_names(self):
        """
        Creates a new column called "state_name" which has the corresponding state name.
        See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        """
        names_map = {
            "AL": "Alabama",
            "CT": "Conn",
            "CA": "Cali",
            "CO": "Colo",
            "DC": "District of Columbia"
        }
        #print(type(self.df["abbrev"])) #> <class 'pandas.core.series.Series'>
        self.df["state_name"] = self.df["abbrev"].map(names_map)
        #return self.df
​
    @staticmethod
    def progress_message():
        print(datetime.now())
​
    def do_stuff(self, my_message):
        print(self.df.columns, my_message)
​
if __name__ == "__main__":
​
    df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    transformer = DataTransformer(df)
    print(transformer.df.head())
    #transformer.convert_names()
    transformer.another_example()
    print(transformer.df.head())
    #transformer.do_stuff("HELLO WEDNESDAY!!!")
​
​
    exit()
​
    print("--------------")
    df2 = pandas.DataFrame({"abbrev": ["GA", "NY", "CA", "CO"]})
    transformer2 = DataTransformer(df2)
    print(transformer2.df.head())
    transformer2.convert_names()
    print(transformer2.df.head())
​
    #df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    #print(type(df)) #> pandas.DataFrame
    #full_df = convert_names(df)
    #print(full_df.head())
#
    #df2 = pandas.DataFrame({"abbrev": ["GA", "NY", "CA", "CO"]})
    #full_df2 = convert_names(df2)
    #print(full_df2.head())
#
    #df = pandas.DataFrame({"a": [1,2,3]})