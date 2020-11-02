import streamlit as st
from lib.base_dfs_and_lists import simple_df
from lib.filter_rows import filter_rows


def exemplo_interatividade_parte_2():
    st.markdown("""
        ## Using interactivity to filter dataframes ##
        
        This example will show in pratice the potential of using
        interactivity to filter dataframes.
        
        You can use this same interactivity (`buttons`, `checkbox`, `selectbox`, etc)
        to modify, **in real time**, plots, methods (like an prediction method only if
        the user chooses a specific input), and much more.
        
        We're not entering in the complexity of filter data in dataframe, just using
        and abstract method that does that.
        """)
    df = simple_df()

    filter_rows_aux_class = filter_rows(sample_df=df)

    row_unique_values = filter_rows_aux_class.return_unique_values_of_column("Role")

    selected_row_value = st.selectbox(
        "Selecione o valor desejado para a coluna Role",
        row_unique_values
    )

    st.markdown(f"The selected value is: `{selected_row_value}`, which have this type `{type(selected_row_value)}`")

    st.markdown("""
        **Below we see 2 dataframes:**
        - First one is filtered by the input (notice that, in order to do this in the code, we had to create a
        new dataframe, filtered by the selected line);
        - Second is the old dataframe, which hasn't suffered any alterations, since it hasn't been overwritten.
    """)

    df_filtrado = filter_rows_aux_class.filter_df_using_selected_rows_values(
        column="Role", row_value=selected_row_value
    )

    st.dataframe(df_filtrado)
    st.dataframe(df)

    st.markdown("""### Lets also change an plot with the input: ###""")
    st.bar_chart(df_filtrado)
    st.markdown("The plot is not that useful, as it converts the index of the rows in values :/")


if __name__ == '__main__':
    exemplo_interatividade_parte_2()
