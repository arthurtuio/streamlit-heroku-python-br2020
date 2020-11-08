import streamlit as st

from lib.base_dfs_and_lists import simple_df, simple_list


def remove_df_or_list_last_row(obj):
    obj = obj[:-1]
    return obj


def exemplo_dataframes():
    st.write("___________________________________")

    st.markdown("""
        ## Bora fazer mais! ##
        
        Vamos trabalhar com **Dataframes**!!
        """)

    st.markdown("### Dataframe vazio: ###")
    st.dataframe()  # o código não vai quebrar, mas dá uma conferida no output

    st.markdown("""
        ### Representacão do dataframe: ###
        
        Vamos usar o método `st.dataframe()`, passando no argumento dele um dataframe!
    """)
    st.dataframe(simple_df())

    st.markdown("""
        ### Representacão de uma lista: ###
        
        Vamos usar o mesmo método de antes, mas passando agora uma lista no argumento,
        pra ver o resultado!
    """)
    st.dataframe(simple_list())  # Isso acontece porque uma lista também é DF de apenas 1 coluna (sem o nome da coluna)
    st.write(f"\n\n Outra representação de lista, passando ela no argumento do `st.write`: {simple_list()}")

    st.markdown("""
        ### Fazendo operações no objeto: ###

        Vamos agora observar o que acontece com a visualização da estrutura (tanto dataframe quanto a lista)
        quando realizamos uma operação nele!
        
        A operação será remover a última linha do mesmo! Para isso vamos usar um método criado neste código,
        o método `remove_df_or_list_last_row()`, que não aparece na visualização do streamlit, apenas
        remove a última linha do dataframe ou lista.
        
        Vamos começar removendo do dataframe!
        """)

    new_df = remove_df_or_list_last_row(simple_df())  # Note que criamos uma nova variável pra armazenar o resultado da operação!
    st.dataframe(new_df)

    st.markdown("Agora para a lista!:")
    new_list = remove_df_or_list_last_row(simple_list())  # Aqui também, nova variável
    st.dataframe(new_list)

    st.markdown("""
        ### O que aprendemos ###

        Você pode mostrar dataframes, listas (tuplas, dicionários, etc) com o streamlit muito facilmente!

        Podemos também realizar operações nestes objetos, no mesmo código!
        
        Mas e interatividade, como faço?
        """)


if __name__ == '__main__':
    exemplo_dataframes()
