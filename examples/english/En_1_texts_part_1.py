import streamlit as st
import pandas as pd
from lib.base_dfs_and_lists import simple_df


def st_text_examples_part_1():
    st.write("Writing texts with Streamlit is super easy :)")

    st.write("You can even jump lines \n \n Yeah!")

    st.write("\n\n")

    my_name = "Arthur"
    my_age = 24

    st.write("And I can also use string formatting! \n")
    st.write(f"My name is: {my_name}! I have {my_age} years old!")

    st.write("\n\n Theres much more things possible with 'write', like trying to do a Dataframe!")
    st.write(pd.DataFrame(simple_df()))


st_text_examples_part_1()
