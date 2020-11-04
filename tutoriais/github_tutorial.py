import streamlit as st

from tutoriais.examples.portugues.heroku.config_github_repo import ConfigGithubRepo

# WIP


class GithubTutorial:

    @staticmethod
    def initialize():
        st.markdown("""
            # Tutorial específico do Github #
            
            **Nesse tutorial vamos aprender como deixar o Github configurado para posteriormente
            realizarmos o deploy no Heroku.**
            
            Novamente, a ideia aqui é que você consiga fazer tudo por conta própria, mas, 
            se precisar de qualquer ajuda, só me procurar!
            
            __________________
        """)

        lista_topicos = [
            "1.Entendendo os arquivos do repo",
            "2.Configurando seu repo"
        ]

        passo_tutorial = st.sidebar.selectbox(
            "Passo a passo tutorial",
            lista_topicos
        )

        if passo_tutorial == lista_topicos[0]:
            ConfigGithubRepo().understanding_repo_objects()

        elif passo_tutorial == lista_topicos[1]:
            ConfigGithubRepo().config_your_repo()


if __name__ == '__main__':
    GithubTutorial().initialize()
