import pandas as pd

class FileToDf:
    """ This class taks a filename and converts it into a pandas data frame
    Returns:
        _type_: pandas dataframe
    """
    def __init__(self, filename):
        self.filename = filename
        self.dataframe = ''
    
    def cvtodf(self):
        self.dataframe = pd.read_csv(self.filename)
        return self.dataframe
    
    def columns(self):
        return self.dataframe.columns
    
    def filterdataframe(self, column, value):
        return self.dataframe[self.dataframe[column] == value]
    
    def sortbycolumn(self, column):
        return self.dataframe.sort_values(by=column)
    
    def sortfilter(self, columntofilter, value, columntosort):
        return self.dataframe[self.dataframe[columntofilter] == value].sort_values(by=columntosort)
    
    def getmedianbycolumn(self, columntofilter, value, column):
        df = self.dataframe[self.dataframe[columntofilter] == value]
        return df[column].median()
    
    def getstdbycolumn(self, columntofilter, value, column):
        df = self.dataframe[self.dataframe[columntofilter] == value]
        return df[column].std()
    
    def getgroupbycolumn(self, columntofilter, columntoagregate):
        return self.dataframe.groupby(columntofilter)[columntoagregate].median().reset_index()
    
    def getfilterbycolumngroupbycolumn(self, columntofilter, value, columntogroup, columntoagg):
        return self.dataframe[self.dataframe[columntofilter] == value].groupby(columntogroup)[columntoagg].median().reset_index()