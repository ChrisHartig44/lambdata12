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

class model_prep
def __init__(self, train, val, test, my_df):
        """
        Params my_df (pandas.DataFrame) with with column called "abbrev" which has state abbrevs
        """
        self.df = my_df.copy()
    def target_features(target):
        '''
        Target = target from the dataframe. 
 
        '''
 
        target = target
        features = train.columns.drop(target)
 
        x_train = train[features]
        y_train = train[target]
        x_val = val[features]
        y_val = val[target]
        x_test = test[features]
        y_test = test[target]
 
        return x_train, y_train, x_val, y_val, x_test, y_test