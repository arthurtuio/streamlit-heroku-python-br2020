import pandas as pd


def simple_df():
    return pd.DataFrame({
        "Names":
            ["Arthur", "Berna", "Claudiomar", "Danilo", "Êrica", "Bellon", "João", "Kauan", "Queiroz"],
        "Role": [
            "Data Eng.",
            "Data Eng.",
            "Data Eng.",
            "Data Sci.",
            "Data Sci.",
            "Data Sci.",
            "Data Eng.",
            "Data Eng.",
            "Data Eng."
        ]
    })


def simple_list():
    return ["Arthur", "Berna", "Claudiomar", "Danilo", "Êrica", "Bellon", "João", "Kauan", "Queiroz"]
