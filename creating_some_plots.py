import pandas as pd
import streamlit as st

from lib.create_plot import CreatePlot


class CreatingSomePlots:
    def __init__(self):
        self.hr_employee_df = pd.read_csv("datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv")
        self.mcdonalds_df = pd.read_csv("datasets/mcdonalds_nutrition_facts.csv")
        self.spotify_df = pd.read_csv("datasets/spotifyclassification.csv")
        self.chocolate_bar_df = pd.read_csv("datasets/chocolate-bar-ratings.csv")
        self.uber_df = pd.read_csv("datasets/uberdrives.csv")
        self.ny_df = pd.read_csv("datasets/new_york_city_airbnb_open_data.csv")

    def _group_dfs_in_list(self):
        return [
            {"name": "hr_employee_df", "df": self.hr_employee_df, "column": "Department"},
            {"name": "mcdonalds_df", "df": self.mcdonalds_df, "column": "Category"},
            {"name": "spotify_df", "df": self.spotify_df, "column": "artist"},
            #{"name": "chocolate_bar_df", "df": self.chocolate_bar_df, "column": "Company"},
            #{"name": "uber_df", "df": self.uber_df, "column": "PURPOSE*"},
            {"name": "ny_df", "df": self.ny_df, "column": "neighbourhood_group"}
        ]

    @staticmethod
    def _create_bar_plot(df, column):
        return CreatePlot(sample_df=df).categorical_count_bar_plot(categorical_column=column)

    def _load_in_streamlit(self, dicionario):
        st.markdown(f"""
            __________

            ### Dataframe {dicionario.get("name")} ###
        """)
        dataframe = dicionario.get("df")

        st.dataframe(dataframe)

        dataframe_column = dicionario.get("column")

        df_to_plot = self._create_bar_plot(dataframe, dataframe_column)

        st.plotly_chart(df_to_plot, use_container_width=True)

    def create_all_plots(self):
        for dicionario in self._group_dfs_in_list():

            self._load_in_streamlit(dicionario)


CreatingSomePlots().create_all_plots()

