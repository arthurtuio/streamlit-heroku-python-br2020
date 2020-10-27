import pandas as pd


def simple_df():
    return pd.DataFrame({
        "Names": [
            "Arthur",
            "Claudiomar",
            "Danilo",
            "Êrica",
            "Evans",
            "Bellon",
            "Lobinho",
            "Hermes",
            "João",
            "Kauan",
            "Dona Naka",
            "Berna",
            "Marilia",
            "Queiroz",
            "Nedson",
            "Phil",
            "Ruan",
            "Thaís",
            "Darta",
            "Wutzke",
            "Vanessa",
            "Will",
            ],
        "Role": [
            "Data Engineer",
            "Data Engineer",
            "Data Scientist",
            "Data Scientist",
            "Data Analyst",
            "Data Scientist",
            "Data Analyst",
            "Data Analyst",
            "Data Engineer",
            "Data Engineer",
            "Data Analyst",
            "Data Engineer",
            "Data Analyst",
            "Data Engineer",
            "Data Analyst",
            "Data Analyst",
            "Data Analyst",
            "Data Analyst",
            "Data Analyst",
            "Data Analyst",
            "Data Analyst",
            "Data Analyst",
        ]
    })


def simple_list():
    return simple_df()["Names"].tolist()
