import streamlit as st

from tutoriais.github_tutorial import GithubTutorial
from tutoriais.streamlit_tutorial import StreamlitTutorial
from tutoriais.heroku_tutorial import HerokuTutorial

global images_folder
images_folder = "tutoriais/examples/portugues/heroku/imagens/"


def ToolsTutorial():
    st.markdown("""
        ________________

        # 6. Tutorial das ferramentas #
        
        Por aqui que iremos navegar por todos os tutoriais.
        
        Todos foram feitos de forma que você consiga avançar por conta própria, mas se mesmo assim
        precisar de uma ajuda pode entrar em contato comigo! (Só ver meus contatos no item 5.)
    """)

    lista_topicos = [
        "6.1.Github",
        "6.2.Streamlit",
        "6.3.Heroku"
    ]

    opcao_selecionada = st.selectbox(
        "Passo a passo tutorial completo:",
        lista_topicos
    )

    st.markdown("____________")

    if opcao_selecionada == lista_topicos[0]:
        GithubTutorial().initialize()

    elif opcao_selecionada == lista_topicos[1]:
        StreamlitTutorial().initialize()

    if opcao_selecionada == lista_topicos[2]:
        HerokuTutorial().initialize()


if __name__ == '__main__':
    ToolsTutorial()
