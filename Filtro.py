import pandas as pd
#from tkinter.filedialog import askopenfilename
import sys
import warnings
warnings.filterwarnings("ignore")


def leer_tabla(nombre_archivo):
    """lee la tabla"""
    df = pd.read_table(nombre_archivo, encoding = "ISO-8859-1")

    df.replace(".",0, inplace=True)
    return df

def numeric(df,columnas):
    """pasar a numerico as columnas seleccionadas do dataframe"""
    for elegida in columnas:
        df[elegida]= pd.to_numeric(df[elegida])

def transformar_columnas(df):
    columnas = ["integrated_fitCons_score",
            "integrated_confidence_value",
            "GERP++_RS",
            "phyloP7way_vertebrate",
            "phyloP20way_mammalian"]
    numeric(df,columnas)

def primer_filtrado(df):
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
    return df_filter

def filtrosXscore(df, scores):
    """filtramos 3 columnas por scores("CADD_phred","GERP++_RS", "DANN_score")"""
    return df[(df["CADD_phred"] >= scores[0])&
        (df["GERP++_RS"] >= scores[1])&
        (df["DANN_score"]> scores[2])&
        (df["DANN_score"] < scores[3])]
    
def segundo_filtrado(df_filter):
    df_stopgain = filtrosXscore(df_filter, [37.0, 2.0, 0.995, 1.0])
    df_splicing = filtrosXscore(df_filter, [17.0, 2.0, 0.995, 0.998])
    df_missense = filtrosXscore(df_filter, [17.0, 2.0, 0.995, 1.0])
    return [df_stopgain, df_splicing, df_missense]

def generar_excel(df_filter):
    df_filter.to_excel("Filtros.xls")

if __name__ == "__main__":
    #nombre_de_archivo = askopenfilename()
    nombre_de_archivo = sys.argv[1]
    df = leer_tabla(nombre_de_archivo)
    transformar_columnas(df)
    df = primer_filtrado(df)
    df_3 = segundo_filtrado(df)

    generar_excel(df)   
