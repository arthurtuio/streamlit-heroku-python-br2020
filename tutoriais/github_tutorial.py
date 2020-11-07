import streamlit as st

from tutoriais.examples.portugues.github.config_github_repo import ConfigGithubRepo


class GithubTutorial:
    @staticmethod
    def initialize():
        st.markdown("""
            # Tutorial específico do Github #
            
            **Nesse tutorial vamos aprender como deixar o Github configurado para
            começarmos a usar o Streamlit, e posteriormente realizarmos o deploy no Heroku.**
            
            __________________
        """)

        lista_topicos = [
            "1.Entendendo os arquivos do repo",
            "2.Configurando seu repo"
        ]

        passo_tutorial = st.selectbox(
            "Passo a passo tutorial",
            lista_topicos
        )

        config_github = ConfigGithubRepo()

        if passo_tutorial == lista_topicos[0]:
            config_github.understanding_repo_objects()

        elif passo_tutorial == lista_topicos[1]:
            config_github.config_your_repo()


if __name__ == '__main__':
    GithubTutorial().initialize()
