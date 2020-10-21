#  Work in Progress
import streamlit as st
from lib.create_plot import CreatePlot
from lib.base_dfs_and_lists import simple_df


def st_plot_example():
    st.markdown("""
        ## Plots!! ##

        For the tutorial, we're not focusing on HOW to use plot libs and make
        super ultra awsome plots, instead, we're focusing on HOW to see a plot 
        in Streamlit. 
        
        Its up to you to make the most awsome plots, and displaying them in
        streamlit using the knowledge aquired here!
        """)
    df = simple_df()
    #print(df)

    st.markdown(f"""
        Lets start converting our friendly dataframe above in a simple bar chart!
        
        Df:
    """)

    st.dataframe(df)

    simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot("Role")
    st.plotly_chart(simple_bar_chart, use_container_width=True)


st_plot_example()