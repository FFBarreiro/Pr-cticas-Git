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

df_stopgain = df_filter[(df_filter["CADD_phred"] >= 37)&
    (df_filter["GERP++_RS"] >= 2)&
    (df_filter["DANN_score"]>0.995)&
    (df_filter["DANN_score"] < 1)]

df_splicing = df_filter[(df_filter["CADD_phred"] >= 17)&
    (df_filter["GERP++_RS"] >= 2)&
    (df_filter["DANN_score"]>0.995)&
    (df_filter["DANN_score"] < 0.98)]

df_missense = df_filter[(df_filter["CADD_phred"] >= 17)&
    (df_filter["GERP++_RS"] >= 2)&
    (df_filter["DANN_score"]>0.995)&
    (df_filter["DANN_score"] < 1)]

df_filter.to_excel("Filtros.xls")
