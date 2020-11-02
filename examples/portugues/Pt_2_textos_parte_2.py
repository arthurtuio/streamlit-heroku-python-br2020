import streamlit as st


def exemplo_textos_parte_2():
    st.title("E usando 'st.title' um título é criado!")

    st.markdown("""
        Pessoalmente, prefiro tudo relacionado a textos usando o `st.markdown`.
        
        Posso escrever tudo o que quero neste bloco e também posso usar **negrito**, _itélicc_,
        tudo o que está disponível em markdown.
        
        #### Também posso criar cabeçalhos! ####
        
        ### Sim ###
        
        ## Cabeçalhos ##
        
        # No mesmo bloco #
        """)

    st.markdown("""
        ### O que aprendemos ###

        Markdown é maravilhoso, e mais maravilhoso ainda é poder usar isso no streamlit
        
        E outros objetos?
        """)


if __name__ == '__main__':
    exemplo_textos_parte_2()
