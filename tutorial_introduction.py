import streamlit as st


class TutorialIntroduction:
    def __init__(self): pass

    def initialize(self):
        st.markdown("""
            # Tutorial Streamlit / Heroku Python Brasil 2020 #
            
            Fala aí!!! Muito obrigado por acessar essa página!!
            
            Aqui você vai encontrar, de forma interativa, conteúdo sobre como criar uma
            aplicação web usando a ferramenta **Streamlit**, a qual permite a criação de aplicações
            de dados performáticas e bonitas, de forma simples, em **Python**, e de graça!
              
            Feito isso, você também vai conseguir aprender sobre como fazer o deploy da mesma,
            ou seja, deixar ela disponível na internet, usando a ferramenta **Heroku**!
            
            Comece selecionando abaixo o item 1, para entender um pouco mais sobre as 
            ferramentas usadas neste tutorial!
            
            A ideia é que você consiga fazer tudo por conta própria, mas se em qualquer momento,
            tiver uma dúvida, pode me procurar! Pra isso, só selecionar a opção `4. Sobre mim e meu contato`        
        """)

        passo_tutorial = st.selectbox(
            "Passo a passo tutorial",
            (
                "1.Tecnologias utilizadas",
                "2.Configurando o ambiente local",
                "3.Inscrição para a Python Brasil 2020",
                "4.Sobre mim e meu contato"
            )
        )

        if passo_tutorial == "1.Tecnologias utilizadas":
            self._descriptions()

        elif passo_tutorial == "2.Configurando o ambiente local":
            self._config_local_environment()

        elif passo_tutorial == "3.Inscrição para a Python Brasil 2020":
            self._subscribe_python_br_2020()

        elif passo_tutorial == "4.Sobre mim e meu contato":
            self._my_contact()

    def _descriptions(self):
        st.markdown("""
            ## **1. Tecnologias Utilizadas Neste Tutorial** ##
            
            Para entender mais sobre as tecnologias, basta fazer a seleção abaixo:
        """)

        resultado = st.selectbox(
            "Qual tecnologia você quer conhecer?",
            ("Streamlit", "Heroku", "Git")
        )

        if resultado == "Streamlit":
            self._streamlit_description()

        elif resultado == "Heroku":
            self._heroku_description()

        elif resultado == "Git":
            self._git_description()

    @staticmethod
    def _config_local_environment():
        st.markdown("""
            ## **2. Configurando o ambiente local** ##
            
            Pra você conseguir rodar o conteúdo dessa aplicação, e criar o conteúdo que quiser usando
            estas ferramentas, existem alguns pré-requisitos que você precisa ter. São eles:
            
                1. Conhecimento básico sobre Python - e também alguma familiaridade com estruturas de dados.
                2. Ter alguma ferramenta (IDE) que permita programar em Python em seu PC (recomendo o PyCharm Community);
        
            Além dessas, se você já entender de Github, vai ver que será muito fácil preprar sua aplicação. 
            **Se você não entende, se inscreve aí na Python Brasil 2020 e vai no meu tutorial!**
            Ou, se a conferência já passou, tá tranquilo, você só vai precisar criar uma conta no Github, 
            e saber usar o comando `git clone`. 
            
            - Pra criar conta é só acessar aqui: https://github.com/join
            - Esse site aqui explica como usar `git clone`: 
            https://docs.github.com/pt/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository
            
            O link pra inscrição da conferência tá no bloco `3. Inscrição para a Python Brasil 2020`
            
            Para configurar o ambiente local, só acessar esse repo e seguir o tutorial do `README`:
            https://github.com/arthurtuio/streamlit-heroku-python-br-2020
            
        """)

    @staticmethod
    def _subscribe_python_br_2020():
        st.markdown("""
            ## **3. Inscrição para a Python Brasil 2020** ##
            
            Sobre a conferência:
            
            ```
            A Python Brasil 2020 é a maior conferência sobre linguagem de programação Python do Brasil e da América Latina.

            Feita pela comunidade para a comunidade, tem o objetivo de difundir a linguagem, disseminar conhecimento,
            promover a troca de experiências e manter a comunidade crescendo igualmente em público e impacto social.
            
            Este ano, em caráter de exceção devido à pandemia de covid-19, a Python Brasil será realizada remotamente,
            organizada por um time distribuído no Brasil e no mundo, a fim de prosseguir com o seu objetivo
            de disseminar conhecimento e aproximar pessoas.

            Serão sete dias de imersão, onde participantes poderão contribuir para projetos de software livre,
            participar de treinamentos e adquirir novos conhecimentos com outras pessoas da comunidade.
            ```
            
            Para se inscrever basta acessar esse site: https://2020.pythonbrasil.org.br/
            Para ver a programação, aqui: https://2020.pythonbrasil.org.br/grade/
            
            **Esse tutorial será dado no domingo, dia 08, das 14h às 17h!**
        """)

    @staticmethod
    def _my_contact():
        st.markdown("""
            ## **4. Sobre mim e meu contato** ##
            
            E aí! Prazer em te conhecer! Uma introdução sobre em ~300 caracteres:
            
            *Sou o Arthur Henrique, Joinvilense, amante de música e videogames, e que me considero um cara
            muito empenhado em ajudar pessoas. Já fui voluntário em vários projetos, passando por áreas bem diferentes.
            Hoje sou engenheiro de dados na Conta Azul, empresa em que aprendi muito do que sei hoje em programação.*
            
            Se tiveres qualquer dúvida sobre esse tutorial, ou quiser bater um papo, pode me mandar mensagem
            nas minhas redes sociais:
            - GitHub: https://github.com/arthurtuio
            - Linkedin: https://www.linkedin.com/in/arthurdellantonia/
            - Instagram: https://www.instagram.com/arthurhdell
        """)

    @staticmethod
    def _streamlit_description():
        st.markdown("""
            ### **Streamlit** ###
            
            De acordo com eles, é a *maneira mais rápida de criar e compartilhar aplicações de dados.*

            A documentação deles é ótima, tornando bem tranquilo o aprendizado da ferramenta por conta própria.

            Para conferir, só acessar o site: https://www.streamlit.io/
            
            Essa página web foi criada usando `streamlit`!
        """)

    @staticmethod
    def _heroku_description():
        st.markdown("""
            ### **Heroku** ###
            
            É uma plataforma de nuvem como serviço (Cloud Platform as a Service - PaaS).
            
            Suporta diversas linguagens de programação.
            
            Permite a criação, execução e operação de aplicações, tudo de forma
            bem simples, tirando aquele stress de mexer com infraestrutura.
            
            Pra saber mais sobre, só acessa o site: https://www.heroku.com/what#
                                    
            Essa página web foi deployada (foi pra internet) usando `heroku`!
        """)

    @staticmethod
    def _git_description():
        st.markdown("""
            ### **Git** ###

            O código de programação desta página (e do resto do tutorial) está 
            armazenado num repositório público do `Github`! 
            Para dar uma olhada, só acessar: 
            
            https://github.com/arthurtuio/streamlit-heroku-python-br-2020
        """)


TutorialIntroduction().initialize()