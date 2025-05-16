
import requests
import zipfile
import io
import pandas as pd
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ANO = 2024
URL = f"https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A{ANO}.ZIP"
ARQUIVO_SAIDA = f"valores_bancos_{ANO}_FILTRADO_CORRIGIDO_FINAL.csv"

instituicoes_keywords = [
    "ABC", "ALFA", "AMAZONIA", "BMG", "PAN", "BANESE", "BANESTES", "BANPARA", "BANRISUL",
    "BR PARTNERS", "BRADESCO", "BRASIL", "BRB", "BTG", "ITAUSA", "ITAU", "MERCANTIL",
    "MODAL", "NORD", "PINE", "SANTANDER", "SOFISA", "NU", "HOLDINGS", "INTER"
]

tickers_adicionais = {"INBR32", "INBR32M", "INBR32T", "NUBR33", "NUBR33T", "ROXO34"}

res = requests.get(URL, verify=False)
with zipfile.ZipFile(io.BytesIO(res.content)) as zip_file:
    nome_arquivo = [n for n in zip_file.namelist() if n.endswith(".TXT")][0]
    with zip_file.open(nome_arquivo) as file:
        linhas = [l.decode("latin1") for l in file if l.startswith(b"01")]

registros = []
for linha in linhas:
    cod_bdi = linha[10:12]
    if cod_bdi not in ["02", "96"]:
        continue
    data = datetime.strptime(linha[2:10], "%Y%m%d").date()
    cod_neg = linha[12:24].strip()
    nome_empresa = linha[27:39].strip()
    tipo_mercado = linha[24:27]
    preabe = int(linha[56:69]) / 100
    preult = int(linha[108:121]) / 100
    if cod_neg in tickers_adicionais or any(n in nome_empresa.upper() for n in instituicoes_keywords):
        registros.append([data, cod_neg, nome_empresa, tipo_mercado, preabe, preult])

df = pd.DataFrame(registros, columns=[
    "DATA", "COD_NEGOCIACAO", "NOME_EMPRESA", "TIPO_MERCADO", "PRECO_ABERTURA", "PRECO_FECHAMENTO"
])
df.to_csv(ARQUIVO_SAIDA, index=False, encoding="utf-8-sig")
print(f"✅ Arquivo salvo como: {ARQUIVO_SAIDA}")
