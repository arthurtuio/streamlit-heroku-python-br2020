import numpy as np
import pandas as pd
import streamlit as st

from examples.english.lib.create_plot import CreatePlot
from examples.english.lib.base_dfs_and_lists import simple_df


def exemplo_plots():
    st.write("___________________________________")

    st.markdown("""
        ## Plots!! ##

        Para o tutorial, não estamos nos concentrando em COMO usar bibliotecas de plot e criar gráficos
        super ultra impressionantes, em vez disso, estamos nos concentrando em COMO ver um gráfico usando o
        Streamlit.
        
        Cabe a você fazer os gráficos mais incríveis e exibí-los na web usando o conhecimento adquirido aqui!
        """)
    df = simple_df()

    st.markdown(f"""
        Vamos começar convertando nosso amigável dataframe em um simples bar chart!

        Pra isso vamos usar `st.dataframe(df)`
        
        Df:
    """)

    st.dataframe(df)

    simple_bar_chart = CreatePlot(sample_df=df).categorical_count_bar_plot("Role")
    st.plotly_chart(simple_bar_chart, use_container_width=True)

    st.markdown("""
        Conseguimos literalmente fazer qualquer tipo de plot, e a forma de adicioná-los na web
        é geralmente usando o mesmo método.

        No caso deste tutorial, como estamos usando a biblioteca **plotly**, o método usado para
        chamar os gráficos é `st.plotly_chart`. Além dela, também é possível mostrar gráficos do **matplotlib**,
        **seaborn**, e várias outras libs.
        
        Além destes, o streamlit também tem alguns métodos de gráficos nativos, como por exemplo:
        - `st.line_chart`;
        - `st.area_chart`;
        - `st.bar_chart`.
    """)

    st.write("Vamos testar um `st.area_chart`:")

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

    st.area_chart(chart_data)


if __name__ == '__main__':
    exemplo_plots
