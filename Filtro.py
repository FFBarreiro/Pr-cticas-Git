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

df["ExonicFunc.refGene"] = df["ExonicFunc.refGene"].astype(str)
df["ExAC_EAS"] = pd.to_numeric(df["ExAC_EAS"])
df["ESP6500siv2_EA"] = pd.to_numeric(df["ESP6500siv2_EA"])
df_filter = df[(~df["ExonicFunc.refGene"].str.contains("unknown")) &
   (~df["ExonicFunc.refGene"].str.startswith("synonymous SNV"))&
   (~df["ExonicFunc.refGene"].str.contains("frameshift deletion|frameshift insertion"))&
   (df["Func.refGene"].str.contains("exonic|splicing"))&
   (df["PopFreqMax"] < 0.001)&
   (df["ExAC_EAS"] < 0.001)&
   (df["ESP6500siv2_EA"] < 0.001)]
