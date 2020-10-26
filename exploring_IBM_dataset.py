import streamlit as st
import pandas as pd
from examples.english.lib.create_plot import CreatePlot
from examples.english.lib.filter_rows import filter_rows

dataset_folder = "/home/arthur/clone_tutorial_streamlit_heroku/streamlit-heroku-python-br-2020/datasets/"
dataset_name = "WA_Fn-UseC_-HR-Employee-Attrition.csv"

dataset = dataset_folder + dataset_name

df = pd.read_csv(dataset)


def st_simple_analysis_ibm_dataset(dataframe):
    st.dataframe(dataframe)

    simple_bar_chart = CreatePlot(sample_df=dataframe).categorical_count_bar_plot("Department")
    st.plotly_chart(simple_bar_chart, use_container_width=True)

    simple_hist_chart = CreatePlot(sample_df=dataframe).histogram_plot(
        x_column="Age",
        color="Gender",
        see_distribution=True
    )
    st.plotly_chart(simple_hist_chart, use_container_width=True)

    st.markdown("Vamos filtrar o dataframe agora")
    row_unique_values = filter_rows(sample_df=dataframe).return_unique_values_of_column("Gender")

    st.markdown(f"{row_unique_values}")
    st.selectbox(
        "Selecione o valor desejado para a coluna Gender",
        row_unique_values
    )


st_simple_analysis_ibm_dataset(df)
