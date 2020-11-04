import streamlit as st

global images_folder
images_folder = "/tutoriais/examples/portugues/heroku/imagens/"


class ConfigGithubRepo:

    def understanding_repo_objects(self):
        st.markdown("""
            # 1.Entendendo os arquivos do repo #
            
            Bom, você já deve imaginar que usaremos de base este repo aqui: 
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
            ## setup.sh ##
            
            Esse código, criado para ser executado no terminal do Linux criado pelo Heroku, traz essas linhas:
            
            ```
            mkdir -p ~/.streamlit/

            echo "\
            [server]\n\
            port = $PORT\n\
            enableCORS = true\n\
            headless = true\n\
            \n\
            " > ~/.streamlit/config.toml
            ```

            Em resumo, o que ele faz é:
            
            1. Criar uma pasta chamada oculta chamada `streamlit` (1ª linha do código);
            
            2. Cria um bloco de texto assim:
            ```
                [server]
                port = 
                enableCORS = true
                headless = true
            ```
            3. Adiciona ele a um arquivo chamado `config.toml`, dentro da pasta `.streamlit` 
            
            Se quiseres rodar esse comando no seu terminal, pra conferir o que tem na pasta `.streamlit`,
            manda bala! Mas muito cuidado porque o seu streamlit local não irá rodar, a menos que você
            exclua o `config.toml` depois!
        """)

    @staticmethod
    def config_your_repo():
        st.markdown("""
             # 2.Configurando seu repo #
             
             O que precisa ser feito é primeiramente um `Fork` deste repositório, isto é,
             você vai criar uma cópia dele, mas na sua conta do Github.
             
             Isso é bem tranquilo, basta clicar no botão `Fork` no canto direito superior do repo.
        """)
        st.image(
            image=images_folder + "repo-2.png",
            caption="Localização do fork no repositório",
            width=800
        )

        st.markdown("""
            _________________
            
            Feito isso, uma nova tela será carregada, com o mesmo repositório, mas na sua conta.
            
            **Com isto, basta clonar este repo para seu Pc.**
            
            Para tal, basta clicar em `Code`, selecionar a opção `HTTPS`, e copiar o código que aparece:
        """)
        st.image(
            image=images_folder + "repo-3.png",
            caption="Localização do link HTTPS de clone no repositório",
            width=800
        )

        st.markdown("""
            _________________

            Abra sua linha de comando/terminal, e digite:

            ```
            git clone <colar o texto que você acabou de copiar do repo>
            ```
            
            Se der certo, aparecerá algo como a imagem:
        """)
        st.image(
            image=images_folder + "repo-4.png",
            caption="Clone do repo feito com sucesso!",
            width=800
        )
