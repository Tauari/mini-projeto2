import csv
import logging
import time
from collections import defaultdict
from functools import wraps

from sqlalchemy import create_engine, text

logging.basicConfig(filename="tempos.log", level=logging.INFO,
                    format="%(asctime)s %(message)s", encoding="utf-8")


def medir_tempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        logging.info("Função '%s' executada em %.6f segundos.", func.__name__, time.perf_counter() - inicio)
        return resultado
    return wrapper


engine = create_engine("postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2")


def LGPD(row):
    id, nome, cpf, email, telefone, nascimento, criado, atualizado = row
    primeiro, *resto = nome.split(" ")
    nome = " ".join([primeiro[0] + "*" * (len(primeiro) - 1), *resto])
    cpf = cpf[:3] + ".***.***-**"
    usuario, dominio = email.split("@")
    email = usuario[0] + "*" * (len(usuario) - 1) + "@" + dominio
    return (id, nome, cpf, email, telefone[-4:], nascimento, criado, atualizado)


def salvar_csv(arquivo, linhas, cabecalho=None):
    with open(arquivo, "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.writer(f)
        if cabecalho:
            escritor.writerow(cabecalho)
        escritor.writerows(linhas)


@medir_tempo
def atividade2(linhas):
    por_ano = defaultdict(list)
    for row in linhas:
        por_ano[row[5].year].append(LGPD(row))
    for ano, registros in por_ano.items():
        salvar_csv(f"{ano}.csv", registros)


@medir_tempo
def atividade3(linhas):
    salvar_csv("todos.csv", [(row[1], row[2]) for row in linhas], ["nome", "cpf"])


with engine.connect() as conn:
    linhas = conn.execute(text("SELECT * FROM usuarios")).fetchall()

atividade2(linhas)
atividade3(linhas)

print("Original:   ", linhas[0])
print("Anonimizado:", LGPD(linhas[0]))
print(len(linhas), "registros processados. Arquivos gerados: um CSV por ano e todos.csv")
print(open("tempos.log", encoding="utf-8").read())
