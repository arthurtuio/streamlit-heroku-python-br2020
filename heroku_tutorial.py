import streamlit as st

from examples.portugues.heroku.config_github_repo import ConfigGithubRepo

# WIP


class HerokuTutorial:
    def initialize(self):
        st.markdown("""
            # Tutorial específico do Heroku #
            
            Nesse tutorial vamos aprender como fazer o processo de deploy de um código em Python usando
            o Heroku.
            
            **Para isto, é exigido que façamos o processo via um repositório do Github.**
            
            Logo, vamos iniciar o tutorial apresentando a estrutura básica de como precisa estar o repositório,
            para depois partirmos para a parte do Heroku (que é super simples!).
            
            Além destes assuntos, no final há uma seção de 'FAQ', ou 'Debug', listando possíveis erros que
            podem acontecer no processo, e a solução para os mesmos!
            
            Novamente, a ideia aqui é que você consiga fazer tudo por conta própria, mas, 
            se precisar de qualquer ajuda, só me procurar!
        """)

        passo_tutorial = st.selectbox(
            "Passo a passo tutorial",
            (
                "1.Configurando seu repositório no Github",
                "2.Textos - parte 2",
                "3.Dataframes",
                "4.Interatividade - parte 1",
                "5.Plots",
                "6.Interatividade - parte 2",
            )
        )

        if passo_tutorial == "1.Configurando seu repositório no Github":
            ConfigGithubRepo().initialize()

        # elif passo_tutorial == "2.Textos - parte 2":
        #     exemplo_textos_parte_2()
        #
        # elif passo_tutorial == "3.Dataframes":
        #     exemplo_dataframes()
        #
        # elif passo_tutorial == "4.Interatividade - parte 1":
        #     exemplo_interatividade_parte_1()
        #
        # elif passo_tutorial == "5.Plots":
        #     exemplo_plots()
        #
        # elif passo_tutorial == "6.Interatividade - parte 2":
        #     exemplo_interatividade_parte_2()


if __name__ == '__main__':
    HerokuTutorial().initialize()
