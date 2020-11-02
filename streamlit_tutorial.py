import streamlit as st

from examples.portugues.Pt_1_textos_parte_1 import exemplo_textos_parte_1
from examples.portugues.Pt_2_textos_parte_2 import exemplo_textos_parte_2
from examples.portugues.Pt_3_dataframes import exemplo_dataframes
from examples.portugues.Pt_4_interatividade_parte_1 import exemplo_interatividade_parte_1
# from examples.portugues.Pt_5_plots import exemplo_plots
# from examples.portugues.Pt_6_Interatividade_parte_2 import exemplo_interatividade_parte_2


class StreamlitTutorial:
    def __init__(self):pass

    def initialize(self):
        st.markdown("""
            # Tutorial específico do Streamlit #
            
            Nesse tutorial vamos explorar algumas funções que tornam o streamlit uma excelente
            biblioteca para aplicações de dados.
            
            Novamente, a ideia aqui é que você consiga fazer tudo por conta própria, mas, 
            se precisar de qualquer ajuda, só me procurar!
        """)

        passo_tutorial = st.selectbox(
            "Passo a passo tutorial",
            (
                "1.Textos - parte 1",
                "2.Textos - parte 2",
                "3.Dataframes",
                "4.Interatividade - parte 1",
                "5.Plots",
                "6.Interatividade - parte 2",
            )
        )

        if passo_tutorial == "1.Textos - parte 1":
            exemplo_textos_parte_1()

        elif passo_tutorial == "2.Textos - parte 2":
            exemplo_textos_parte_2()

        elif passo_tutorial == "3.Dataframes":
            exemplo_dataframes()

        elif passo_tutorial == "4.Interatividade - parte 1":
            exemplo_interatividade_parte_1()

        elif passo_tutorial == "5.Plots":
            st.title("Work In Progress")

        elif passo_tutorial == "6.Interatividade - parte 2":
            st.title("Work In Progress")


if __name__ == '__main__':
    StreamlitTutorial().initialize()