import streamlit as st
import pandas as pd
from examples.english.lib.base_dfs_and_lists import simple_df


def exemplo_textos_parte_1():
    st.write("___________________________________")

    st.write("Escrever textos com o streamlit é super fácil :)")

    st.write("É possível pular linhas usando o famigerado `\ n` \n \n")

    st.write("\n\n")

    my_name = "Arthur"
    my_age = 24

    st.write("E também é possível usar string format!! \n")
    st.write(f"Meu nome é: {my_name}! Eu possuo {my_age} anos!")

    st.write(
        "\n\n E é possível fazer diversas outras coisas com o comando write, como por exemplo escrever um dataframe!"
    )
    st.write(pd.DataFrame(simple_df()))


if __name__ == '__main__':
    exemplo_textos_parte_1()
