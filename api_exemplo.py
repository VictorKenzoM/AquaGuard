from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib

app = FastAPI(title="AquaGuard - API de Classificação de Risco")
modelo = joblib.load("modelo_risco_enchente.joblib")

class DadosRegiao(BaseModel):
    chuva_24h_mm: float = Field(ge=0)
    nivel_rio_m: float = Field(ge=0)
    saturacao_solo_pct: float = Field(ge=0, le=100)
    drenagem_pct: float = Field(ge=0, le=100)
    altitude_m: float = Field(ge=0)

@app.get("/")
def inicio():
    return {"projeto": "AquaGuard", "mensagem": "API de demonstração"}

@app.post("/avaliar-risco")
def avaliar_risco(dados: DadosRegiao):
    entrada = pd.DataFrame([dados.model_dump()])
    try:
        classe = modelo.predict(entrada)[0]
        probabilidades = modelo.predict_proba(entrada)[0]
        return {
            "classificacao": str(classe),
            "probabilidades": {
                str(c): round(float(p), 4)
                for c, p in zip(modelo.classes_, probabilidades)
            },
            "aviso": "Protótipo acadêmico com dados sintéticos; não usar para decisões reais."
        }
    except Exception as erro:
        raise HTTPException(status_code=500, detail=str(erro))
