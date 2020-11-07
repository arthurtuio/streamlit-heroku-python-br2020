import streamlit as st

from examples.lib.base_dfs_and_lists import simple_df
from examples.lib.filter_rows import filter_rows


def exemplo_interatividade_parte_2():
    st.write("___________________________________")

    st.markdown("""
        ## Usando interatividade pra filtrar dataframes ##
        
        Este exemplo mostrará na prática o potencial de uso
        interatividade para filtrar dataframes.
        
        Você pode usar esta mesma interatividade (`button`,`checkbox`, `selectbox`, etc)
        para modificar, ** em tempo real **, gráficos, métodos (como um método de previsão apenas se
        o usuário escolhe uma entrada específica) e muito mais.
        
        Não estamos entrando na complexidade do filtro de dados no dataframe, apenas usando
        e método abstrato que faz isso.
        """)
    df = simple_df()

    filter_rows_aux_class = filter_rows(sample_df=df)

    row_unique_values = filter_rows_aux_class.return_unique_values_of_column("Role")

    selected_row_value = st.selectbox(
        "Selecione o valor desejado para a coluna Role",
        row_unique_values
    )  # tenta trocar esse `st.selectbox()` por um `st.sidebar.selectbox()`

    st.markdown(f"O valor selecionado é: `{selected_row_value}`, que tem esse tipo: `{type(selected_row_value)}`")

    st.markdown("""
        **Abaixo vemos 2 dataframes:**
        - O primeiro é filtrado pela entrada (observe que, para fazer isso no código, tivemos que criar um
        novo dataframe, filtrado pela linha selecionada);
        - Já o segundo é o dataframe antigo, que não sofreu alterações, uma vez que não foi sobrescrito.
    """)

    df_filtrado = filter_rows_aux_class.filter_df_using_selected_rows_values(
        column="Role", row_value=selected_row_value
    )

    st.dataframe(df_filtrado)
    st.dataframe(df)

    st.markdown("""
        Pra saber mais o que é possível fazer usando interação, dá uma conferida no código do 
        `introduction_tutorial.py`, especialmente pro tópico `4.Um pouco do que você pode fazer com essa ferramenta`.
    """)


if __name__ == '__main__':
    exemplo_interatividade_parte_2()
