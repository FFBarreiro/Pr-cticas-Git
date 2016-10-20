import pandas as pd


df = pd.read_table("Variants.tab", encoding = "ISO-8859-1")

df.replace(".",0, inplace=True)

def numeric(df,columnas):
    """pasar a numerico as columnas seleccionadas do dataframe"""
    for elegida in columnas:
        df[elegida]= pd.to_numeric(df[elegida])

columnas = ["integrated_fitCons_score",
            "integrated_confidence_value",
            "GERP++_RS",
            "phyloP7way_vertebrate",
            "phyloP20way_mammalian"]
numeric(df,columnas)
