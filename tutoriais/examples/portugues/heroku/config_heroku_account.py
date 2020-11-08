import streamlit as st

global images_folder
images_folder = "tutoriais/examples/portugues/heroku/imagens/"


class ConfigHerokuAccount:

    @staticmethod
    def creating_account():
        st.markdown("""
            # 2.Criando conta no Heroku #
            
            Acesse a plataforma por aqui: https://www.heroku.com/
            
            Criar uma conta é extremamente simples, basta preencher os dados do `sign up`.
            
            Feito isso, você vai receber um email deles, pedindo para você ativar sua conta.
            
            Após clicar no link de ativação, uma tela como a da imagem abaixo deve aparecer!
        """)
        st.image(
            image=images_folder + "heroku-1.png",
            caption="Tela de ativação da conta",
            width=800
        )

        st.markdown("""
            ________________________
            
            **Clique no botão pra prosseguir, e uma imagem como a de baixo aparecerá,
            referente aos termos de serviço**
        """)
        st.image(
            image=images_folder + "heroku-2.png",
            caption="Tela dos termos de serviço",
            width=800
        )

        st.markdown("""
            ________________________

            **Após aceitar os mesmos, você será redirecionado para a tela de 
            dashboards, conforme imagem abaixo:**
        """)
        st.image(
            image=images_folder + "heroku-3.png",
            caption="Tela de dashboards",
            width=800
        )

        st.markdown("""
            ________________________

            **Clique em criar um novo app, dê um título top pro seu app, pode escolher
            a região Estados Unidos mesmo, e aí clique em criar app!**
            
            Feito isso, você será redirecionado para uma tela como essa:
        """)
        st.image(
            image=images_folder + "heroku-4.png",
            caption="Tela de criação de app",
            width=800
        )

        st.markdown("""
            ________________________
            
            ### Com tudo isso feito, já podemos começar a preprar o deploy! ###
        """)

    @staticmethod
    def preparing_deploy():
        st.markdown("""
            # 3.Fazendo o Deploy no Heroku #

            Já na tela da sua aplicação, a primeira coisa que você precisará fazer
            (e uma das únicas) é, no campo `Deployment method`, escolher a opção `GitHub`.
            
            Após escolher, você só precisa escolher qual repositório da sua conta que será usado
            de base, conforme a imagem abaixo ilustra:
        """)
        st.image(
            image=images_folder + "deploy-1.png",
            caption="Escolhendo qual repo do Git será usado de base",
            width=700
        )

        st.markdown("""
            _____________________
            
            - Clique em `Search`.
            
            - Seu repositório irá aparecer, aí é só clicar em `Connect`.
            
            Novos tópicos aparecerão:
        """)
        st.image(
            image=images_folder + "deploy-2.png",
            caption="Configurando o deploy",
            width=700
        )

        st.markdown("""
            _____________________

            **Como este tutorial é introdutório**, não vamos precisar alterar
            nenhum dos dados selecionados, apenas clicar em `Deploy Branch`.
            
            Feito isso, uma janela irá aparecer, com o título `Build Master`, e um ID na sequência,
            que é o ID do `commit` em questão.
        """)
        st.image(
            image=images_folder + "deploy-3.png",
            caption="Heroku fazendo o build do seu repo",
            width=700
        )

        st.markdown("""
            _____________________

            **Se tudo deu certo, sucesso demais 👏👏👏👏👏**
            
            **Se algo deu errado, dá uma conferida no tópico `4.FAQ/Debuggando erros`,
            que lá provavelmente tem a solução!**

            Para ver seu app, só clicar em `View`:
        """)
        st.image(
            image=images_folder + "deploy-4.png",
            caption="Hora da verdade do seu app",
            width=700
        )

    @staticmethod
    def faq_debugging():
        st.markdown("""
            # 4.FAQ/Debuggando erros #

            Aqui foram listados alguns erros que eu tive durante o desenvolvimento
            da aplicação, os quais, se você vir a ter também, pode checar aqui a solução!
            
            ____________________

            
            ### `Application Error` no site ##
            
            Se apareceu esse erro, a primeira coisa para debuggarmos é ver o `log` de erro do
            Heroku.
            
            Pra fazer isso, basta rodar esse comando no terminal:
            ```
            heroku logs --tail --app your_app_name
            ```
            
            Se o que apareceu foi: **`error code=H10`**:
            - Um possível motivo pra esse erro é que nome da aplicação está errado no `Procfile`
            
            ____________________
            
            ### `src refspec master does not match any` ###
            
            Se na hora que você foi fazer `git push heroku master`, apareceu esse erro, a solução que
            resolveu no meu caso foi bem simples, só precisei digitar isso no terminal:
            ```
            git push heroku HEAD:master
            ```
            - Uma explicação pra ela se encontra aqui: https://stackoverflow.com/questions/8196544/what-are-the-git-concepts-of-head-master-origin/8196578#8196578
            
            ____________________
            
            Se no log veio outro erro, ou aconteceu algo errado em outra etapa, tente capturar o nome
            desse erro, e aí minha dica é usar o google. Também posso te ajudar a procurar
            pela solução na internet :) 
            
            O mais importante é descobrir qual foi o erro, a solução com certeza existe na internet!
        """)