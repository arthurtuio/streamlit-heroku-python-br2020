import streamlit as st


class ConfigGithubRepo:
    def understanding_repo_objects(self):

    def config_repo(self):  # PRECISA TER UM FORK
        st.markdown("# 1.Configurando seu repositório no Github #")

        passo_tutorial = st.selectbox(
            "Esse tópico é gradinho, logo, vamos ver ele em partes",
            (
                "1.Para ",
                "3.Dataframes",
                "4.Interatividade - parte 1",
                "5.Plots",
                "6.Interatividade - parte 2",
            )
        )
