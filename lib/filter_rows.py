import pandas as pd


class filter_rows:
    def __init__(self, sample_df):
        self.sample_df = sample_df

    def return_unique_values_of_column(self, column):
        """
        Method to return the unique values of a column.

        This return can be used with streamlit as a input to filter all the dataframe
        :return: An list with the unique values of the input column.
        """
        return self.sample_df[column].unique().tolist()

    def filter_df_using_selected_rows_values(self, column, row_value):
        """
        Filter the dataframe to return only the values of a present column.

        Can be called in sequence to filter more rows.
        :param row_value: The desired value to filter
        :param column: The column that you want to apply the filter
        :return: The df filtered.
        """
        if type(row_value) == str:
            query = f"{column} == '{row_value}'"
        else:
            query = f"{column} == {row_value}"

        return self.sample_df.query(query)
