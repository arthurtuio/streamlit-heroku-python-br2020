import streamlit as st
from lib.base_dfs_and_lists import simple_df, simple_list


def remove_df_or_list_last_row(obj):
    obj = obj[:-1]
    return obj


def st_dataframes_example():
    st.markdown("""
        ## But lets do more! ##
        
        Like playing with our favorite data structure: **Dataframes**!!
        """)

    st.markdown("### Empty df: ###")
    st.dataframe()  # the code won't break, but look at the output!

    st.markdown("### df representation: ###")
    st.dataframe(simple_df())

    st.markdown("### list representations: ###")
    st.dataframe(simple_list())  # A list is also a DF with only 1 column (without the column name)
    st.write(f"\n\n Another representation of the list: {simple_list()}")

    st.markdown("""
        ### Doing an operation with the obj: ###

        First removing the df last row:

        """)

    new_df = remove_df_or_list_last_row(simple_df())
    st.dataframe(new_df)

    st.markdown("Now removing list last row")
    new_list = remove_df_or_list_last_row(simple_list())
    st.dataframe(new_list)

    st.markdown("""
        ### What we learned ###

        You can show dataframes, lists (and also dicts) in the screen easily.

        You can make operations in those objects in the same code that you use streamlit.
        
        But what about the interactivity?
        """)


st_dataframes_example()
