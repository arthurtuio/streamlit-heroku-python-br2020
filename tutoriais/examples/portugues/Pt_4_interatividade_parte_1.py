import streamlit as st

from tutoriais.examples.portugues.Pt_1_textos_parte_1 import exemplo_textos_parte_1
from tutoriais.examples.portugues.Pt_3_dataframes import exemplo_dataframes


def exemplo_interatividade_parte_1():
    st.write("___________________________________")

    st.markdown("""
        ## Interatividade !! ##

        Para mim, é isso que torna o `streamlit` uma excelente ferramenta.
        
        Há muito que podemos fazer em relação à interatividade!
        
        Como, por exemplo, ** criar um botão: **
        """)
    if st.button('Aperte esse botão'):
        st.write("_Não aconteceu nada! (ou aconteceu?)_")

    st.markdown("**Ou criar uma checkbox:**")  # Tente botar essa linha de código dentro do if ali de cima!
    st.checkbox("Posso adicionar qualquer texto aqui")  # Tenta trocar esse texto


    st.markdown("**Ou um slider!!!**")
    st.slider(
        label="Titulo maravilhoso pro slider", min_value=0, max_value=10
    )

    st.markdown("""
        Também podemos usar esses métodos para chamar outros métodos ou usar seu retorno!
    
        Por exemplo, chamar os outros métodos de exemplo se um botão for pressionado!
    """)
    if st.button('Texts Example'):
        st.write("_Perceba que esse texto abaixo é o do módulo_ `1.Textos - parte 1`")
        exemplo_textos_parte_1()  # Chamo aqui um método desse .py ou qualquer outro, desde que feito o import.

    if st.button('Dataframes Example'):
        st.write("_E esse é do módulo_ `3.Dataframes`")
        exemplo_dataframes()  # Olha que loucura né

    if st.button("*INFORMAÇÃO SUPER IMPORTANTE!*"):
        st.markdown("""
            ### Importante  ###
    
            Depois que um botão é clicado, ele não pode ser desmarcado. Você só pode selecionar 
            outro botão, que fará com que o último seja 'desmarcado'.
        """)

    if st.checkbox("Trabalhando com o retorno dos métodos que permitem interatividade"):
        st.markdown("""
            # **Trabalhando com o retorno dos métodos que permitem interatividade** #
            
            Olha que legal, os métodos do streamlit de interatividade, quando clicados, 
            fazem a mudança na aplicação web porque o valor deles mudou.
            
            Conseguimos associar estes métodos a variáveis, pra capturar esses valores.
        """)

        checkbox_return = st.checkbox("Clica aqui nessa checkbox")
        if checkbox_return:
            button_return = st.button("Secret button")

        st.markdown(f"""
            Fazemos a associação dessa forma:
            
            `checkbox_return = st.checkbox("Clica aqui nessa checkbox")`
            
            E aí podemos usar essa variável livremente no nosso código!
                        
            Vamos começar conhecendo o tipo dessa variável!
            
            `type(checkbox_return) == {type(checkbox_return)}`
        """)

        if checkbox_return:
            st.markdown(f"""
                **Vamos descobrir agora o tipo de um botão:**
                `type(button_return) == {type(button_return)}`

                Bool!
            """)

            if button_return:
                st.markdown("""
                    ## Importantante!!!!!! ##
                    
                    **É uma péssima prática usar o retorno de um botão pra triggar outra parte do código**
                    
                    Isso porque, depois de clicar em qualquer outra coisa, como um slider (ou checkbox ou botão),
                    o botão será 'desselecionado', tornando seu valor bool = False :(
                """)
                slider_return = st.slider(label="Slider secreto", min_value=0, max_value=10)

    st.write("____________________________________________________")

    if st.checkbox("Seção `O que aprendemos`"):
        st.markdown("""
            ### O que aprendemos ###

            Coisa pra caramba!!
                        
            A última coisa que queria compartilhar com você é como usar plots!!!!!    
        """)


if __name__ == '__main__':
    exemplo_interatividade_parte_1()