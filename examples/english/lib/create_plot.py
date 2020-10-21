import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


class CreatePlot:
    def __init__(self, sample_df):
        self.sample_df = sample_df

    def categorical_count_bar_plot(self, categorical_column):
        y_values = self.sample_df[categorical_column].value_counts().tolist()

        x_values = self.sample_df[categorical_column].unique().tolist()

        fig = px.bar(data_frame=self.sample_df, x=x_values, y=y_values)

        plt.figure(
            figsize=(8, 4),
            dpi=80,
            #title_text=f"Bar chart categorical using column {categorical_column}",
        )

        return fig
