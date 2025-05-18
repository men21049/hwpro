import pandas as pd

class FileToDf:
    """ This class taks a filename and converts it into a pandas data frame
    Returns:
        _type_: pandas dataframe
    """
    def __init__(self, filename):
        """_summary_

        Args:
            filename (_type_): file to convert from csv to data frame
        """
        self.filename = filename
        self.dataframe = ''
    
    def cvtodf(self):
        """ method to convert a file into a pandas dataframe
        Returns:
            _dataframe_: pandas dataframe
        """
        self.dataframe = pd.read_csv(self.filename)
        return self.dataframe
    
    def columns(self):
        """ method to list all columns in a data frame
        Returns:
            _list_: list of columns 
        """
        return self.dataframe.columns
    
    def filterdataframe(self, column, value):
        """ Method to filter a dataframe using the column name to filter and value as parameters

        Args:
            column (_string_): column to filter the data frame
            value (_any_): value to filter the column

        Returns:
            _dataframe_: dataframe with filtered data
        """
        return self.dataframe[self.dataframe[column] == value]
    
    def sortbycolumn(self, column):
        """ Method to sort a dataframe by a column

        Args:
            column (_string_): column to order the data frame by

        Returns:
            _dataframe_: dataframe with order data
        """
        return self.dataframe.sort_values(by=column)
    
    def sortfilter(self, columntofilter, value, columntosort):
        """Method to filter and sort a dataframe

        Args:
            columntofilter (_string_): Column to filter the data frame
            value (_any_): value to filter the data frame
            columntosort (_string_): Column to use to order the data frame

        Returns:
            _dataframe_: dataframe with order data
        """
        return self.dataframe[self.dataframe[columntofilter] == value].sort_values(by=columntosort)
    
    def getmedianbycolumn(self, columntofilter, value, column):
        """Method to get the average by column in a data frame

        Args:
            columntofilter (_string_): column to filter te data frame 
            value (any): value of the column to filter by
            column (_string_): column to calculate the average

        Returns:
            _dataframe_: dataframe
        """
        df = self.dataframe[self.dataframe[columntofilter] == value]
        return df[column].median()
    
    def getstdbycolumn(self, columntofilter, value, column):
        """Method to calculate the standard deviation of a column

        Args:
            columntofilter (_string_): column to filter te data frame 
            value (any): value of the column to filter by
            column (_string_): column to calculate the standard deviation

        Returns:
            _dataframe_: dataframe
        """
        df = self.dataframe[self.dataframe[columntofilter] == value]
        return df[column].std()
    
    def getgroupbycolumn(self, columntofilter, columntoagregate):
        """Method to goup the dataset and calculate the average of a column

        Args:
            columntofilter (_string_): column to use as a group by
            columntoagregate (_string_): column to agreggate by

        Returns:
            _dataframe_: dataframe
        """
        return self.dataframe.groupby(columntofilter)[columntoagregate].median().reset_index()
    
    def getfilterbycolumngroupbycolumn(self, columntofilter, value, columntogroup, columntoagg):
        """Method to filter, group by, and calculate the average of a column

        Args:
            columntofilter (_string_): column to use as a filter
            value (_any_): value to filter the columnfilter
            columntogroup (_string_): column or columns to group by
            columntoagg (_string_): column that the average will be calculated

        Returns:
            _type_: _description_
        """
        return self.dataframe[self.dataframe[columntofilter] == value].groupby(columntogroup)[columntoagg].median().reset_index()