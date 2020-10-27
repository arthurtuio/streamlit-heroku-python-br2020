import streamlit as st
import pandas as pd
import numpy as np
from lib.create_plot import CreatePlot
from lib.base_dfs_and_lists import simple_df


def st_plot_example():
    st.markdown("""
        ## Plots!! ##

        For the tutorial, we're not focusing on HOW to use plot libs and make
        super ultra awesome plots, instead, we're focusing on HOW to see a plot 
        in Streamlit.
        
        Its up to you to make the most awesome plots, and displaying them in
        streamlit using the knowledge acquired here!
        """)
    df = simple_df()

    st.markdown(f"""
        Lets start converting our friendly dataframe above in a simple bar chart!
        
        Df:
    """)

    st.dataframe(df)

    simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot("Role")
    st.plotly_chart(simple_bar_chart, use_container_width=True)

    st.markdown("""
        We can make every type of plot, and just call then using the same way.
        
        Particularly, because we're using the lib plotly, the method used in this code
        to call those plots is `st.plotly_chart`, but we can use lots of other methods, like those:
        - `st.line_chart`;
        - `st.area_chart`;
        - `st.bar_chart`;
        - And many more!
    """)

    st.write("Lets just see the implementation of an `st.area_chart`:")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    st.area_chart(chart_data)


st_plot_example()
