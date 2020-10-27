import streamlit as st


def st_text_examples_part_2():
    st.title("And with 'st.title' a title is created!")

    st.markdown("""
        Personally, i prefer to everything related to texts with `st.markdown`.
        
        I can write everything I want in this block, and can also use **bold**, _italic_, 
        everything that's available in markdown.
        
        #### I can also create headers! ####
        
        ### Yep ###
        
        ## Headers ##
        
        # On the same block #
        """)

    fav_food = "Cheeseburguer"

    st.markdown(
        f"And of course I can use string formatting! In this case to tell that my fav food is: **{fav_food}**!!"
    )

    st.markdown("""
        ### What we learned ###

        Markdown is awesome, and we can use it here!
        
        But what about other objects?
        """)


st_text_examples_part_2()
