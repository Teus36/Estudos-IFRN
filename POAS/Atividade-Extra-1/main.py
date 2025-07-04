from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

@app.get("/buscar/{id}")
def buscar_por_id(id: str):
    try:
        df = pd.read_csv("20250702_Pedidos_csv_2025.csv", sep=';', encoding='utf-16')  # Ajusta o separador se precisar
        resultado = df[df["IdPedido"] == id]

        if not resultado.empty:
            return resultado.iloc[0].to_dict()
        else:
            return {"error": "ID não encontrado"}

    except Exception as e:
        return {"error": str(e)}