import streamlit as st
from En_1_texts_part_1 import st_text_examples_part_1
from En_2_texts_part_2 import st_text_examples_part_2
from En_3_dataframes import st_dataframes_example


def exemplo_interatividade_parte_1():
    st.markdown("""
        ## Interactivity!! ##

        For me, this is what makes `streamlit` an excellent tool.
        
        Theres so much we can do about interactivity!
        
        Like, for example, **creating a button:**
        """)
    st.button('Press this button')  # Here we just created it!

    st.markdown("**Or creating a checkbox:**")
    st.checkbox("Press this checkbox")  # And here an checkbox!

    st.markdown("Or a slider!!!")
    st.slider(
        label="Awsome Slider", min_value=0, max_value=10
    )

    st.markdown("""
    We can also use those methods to call another methods, or use their return!
    
    Like, calling the other examples methods if an button is pressed!
    """)
    if st.button('Texts Example'):
        st_text_examples_part_1()  # Calling the
        st_text_examples_part_2()

    if st.button('Dataframes Example'):
        st_dataframes_example()

    if st.button("**Super Important Information**"):
        st.markdown("""
            ## Important  ##
    
            Once an button is clicked, it cannot be unclicked. You can only select another button, which
            will make the last one be 'unclicked'.
        """)

    if st.checkbox("Working with buttons/checkbox return"):
        st.markdown(" # **Working with buttons/checkbox return** #")

        checkbox_return = st.checkbox("Hit this checkbox")
        if checkbox_return:
            button_return = st.button("Secret button")

        st.markdown(f"""
            We can assign any streamlit method with an variable, like that:
            
            `checkbox_return = st.checkbox("Hit this checkbox")`
            
            And use that variable in our code freely!
            
            Lets first examine this variable type:
            
            `type(checkbox_return) == {type(checkbox_return)}`
        """)

        if checkbox_return:
            st.markdown(f"""
                **And now the type of a button variable:**
                `type(button_return) == {type(button_return)}`

                Bool!
            """)

        if button_return:
            st.markdown("""
                ## Important!!!!!! ##
                **Its not a good pratice to use the return of the button to trigger another code.**
                
                Because, once you click anything else, like that slider, the button will be 'unpressed', 
                making its bool value = False :( 
            """)
            slider_return = st.slider(label="Secret Slider", min_value=0, max_value=10)

    st.write("____________________________________________________")

    if st.checkbox("What we learned section"):
        st.markdown("""
            ### What we learned ###

            We learned a lot!
            
            The last basic thing to learn is to make plots!!!!
            
            """)


if __name__ == '__main__':
    exemplo_interatividade_parte_1()