import streamlit as st
from lib.base_dfs_and_lists import simple_df
from lib.filter_rows import filter_rows


def st_interactivity_example_part_2():
    st.markdown("""
        ## Filtering Dataframes through interactivity ##
        
        Aqui a gente vai brincar de filtrar dataframes usando interatividade.
        
        Pra isso, primeiro precisamos criar uma selectbox para o usuário.
        
        Vamos fazer a filtragem do dataframe usando uma classe auxiliar, para focarmos 
        mais na interatividade que o streamlit permite
        
        """)
    df = simple_df()

    filter_rows_aux_class = filter_rows(sample_df=df)

    row_unique_values = filter_rows_aux_class.return_unique_values_of_column("Role")

    selected_row_value = st.selectbox(
        "Selecione o valor desejado para a coluna Role",
        row_unique_values
    )

    st.markdown(f"O valor selecionado é assim: `{selected_row_value}`, do tipo `{type(selected_row_value)}`")

    st.markdown("""
        **Abaixo vemos dois dataframes:**
        - O primeiro é filtrado pela entrada (perceba que para isso no código tivemos que criar um
        novo dataframe, filtrado pela linha selecionada.
        
        - O segundo é o dataframe antigo, que não sofreu alterações, porque em nenhum momento
        foi sobrescrito.
        
    """)

    df_filtrado = filter_rows_aux_class.filter_df_using_selected_rows_values(
        column="Role", row_value=selected_row_value
    )

    st.dataframe(df_filtrado)
    st.dataframe(df)


st_interactivity_example_part_2()