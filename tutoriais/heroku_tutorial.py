import streamlit as st

from examples.portugues.heroku.config_heroku_account import ConfigHerokuAccount

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
            
            __________________
        """)

        lista_topicos = [
            "1.Revisão do que vemos até aqui",
            "2.Criando conta no Heroku",
            "3.Fazendo o Deploy no Heroku",
            "4.FAQ/Debuggando erros"
        ]

        passo_tutorial = st.sidebar.selectbox(
            "Passo a passo tutorial",
            lista_topicos
        )

        if passo_tutorial == lista_topicos[0]:
            self.what_we_saw_until_now()

        elif passo_tutorial == lista_topicos[1]:
            ConfigHerokuAccount().creating_account()

        elif passo_tutorial == lista_topicos[2]:
            ConfigHerokuAccount().preparing_deploy()

    @staticmethod
    def what_we_saw_until_now():
        st.markdown("""
            # 1. Revisão do que vimos até aqui
        
            Se você chegou nesse código, ou foi porque você está no tutorial da Python Brasil, 
            ou porque provavelmente explorou esses dois outros códigos antes:
            - A introdução do tutorial: https://streamlit-heroku-python-br2020.herokuapp.com/;
            - O tutorial do github: https://github.com/arthurtuio/streamlit-heroku-python-br2020/blob/master/tutoriais/github_tutorial.py
            - O tutorial do streamlit: https://github.com/arthurtuio/streamlit-heroku-python-br2020/blob/master/tutoriais/streamlit_tutorial.py
            
            O que implica que você também:
            - Clonou o repositório no seu pc;
            - Já entendeu como usar o comando `streamlit run {codigo}`, e também conhece os métodos do streamlit.
            
            Se você não fez isso ainda, por favor, dá uma conferida neles antes. 
            
            Ou, se quiseres pular direto pra parte do Heroku, tudo bem, sem problemas :)
        """)


if __name__ == '__main__':
    HerokuTutorial().initialize()
