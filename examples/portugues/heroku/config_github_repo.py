import streamlit as st

global images_folder
images_folder = "examples/portugues/heroku/imagens/"


class ConfigGithubRepo:

    def understanding_repo_objects(self):
        st.markdown("""
            # 2.Entendendo os arquivos do repo #
            
            Bom, você já sabe que vamos usar como base esse repositório:
            https://github.com/arthurtuio/streamlit-heroku-python-br2020
            
            **Os arquivos que são necessários para o deploy do heroku são:**
            - Procfile
            - setup.sh
            - O código python (`.py`) que contém a aplicação do streamlit
            que você deseja que vá para o ar.
            
            É sobre cada um destes arquivos que iremos falar na sequência:
        """)

        passo_tutorial = st.selectbox(
            "Selecione o arquivo que deseja entender",
            ("Procfile", "setup.sh", "Código em Python da aplicação")
        )

        if passo_tutorial == "Procfile":
            self._understanding_procfile()

        elif passo_tutorial == "setup.sh":
            self._understanding_setup_sh()

    @staticmethod
    def _understanding_procfile():
        st.markdown("""
             ## Procfile ##

             Pra mim, o que há de mais estranho nesse arquivo, é que ele não tem formato (_não é
             Procfile.algo, é só Procfile_).

             Mas bem, apesar de ser estranho, **esse arquivo é tão importante para o Heroku, que sem ele
             não conseguimos fazer o deploy de nossa aplicação.**

             Se você abrir o arquivo (https://github.com/arthurtuio/streamlit-heroku-python-br2020/blob/master/Procfile),
             vai ver que ele possui incríveis 1 linha de código. Essa linha:

             ```
             web: sh setup.sh && streamlit run introduction_tutorial.py
             ```
             
             **No momento que sua aplicação do Heroku foi criada, o que acontece por debaixos dos panos,
             é que eles lançam uma máquina virtual com Linux, que é responsável pelo servidor da sua aplicação.**
             
             O Procfile é o arquivo que armazena quais comandos serão executados por essa máquina, por isso
             que eles estão em linguagem Linux.
            
             O que cada parte dessa linha de comando significa é:
             - `web`: Estamos dizendo para o Heroku que é uma aplicação web;
             - `sh setup.sh`: 
                 - `sh` sozinho é um comando executado para abrir/executar arquivos `.sh`
                 - `setup.sh` é o arquivo de configuração inicial da nossa máquina virtual.
                O conteúdo dela será explicado no tópico de seu nome.
            """)

    @staticmethod
    def _understanding_setup_sh():
        st.markdown("""
            WIP
        """)

    @staticmethod
    def config_your_repo():  # PRECISA TER UM FORK
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
