# Mini Projeto 2 - LGPD

Trabalho da disciplina de Linguagem de Programação II (FATEC Rio Claro).

O programa se conecta a um banco de dados com 20 mil usuários fictícios e esconde parte dos dados pessoais deles, como pede a LGPD (Lei Geral de Proteção de Dados).

## O que o programa faz

- **Anonimiza os dados:** mostra só o começo do nome, do CPF e do e-mail e só o final do telefone.

  | Campo | Antes | Depois |
  |---|---|---|
  | Nome | Olivia Araújo | O***** Araújo |
  | CPF | 237.615.809-59 | 237.\*\*\*.\*\*\*-\*\* |
  | E-mail | nuneserick@example.com | n*********@example.com |
  | Telefone | +55 (011) 9483-6810 | 6810 |

- **Cria um arquivo por ano de nascimento:** `1990.csv`, `1991.csv` e assim por diante, com os dados já anonimizados.
- **Cria o `todos.csv`:** tem só nome e CPF de todo mundo, sem anonimizar.
- **Mede o tempo:** o tempo de criação dos arquivos fica salvo em `tempos.log`.

## Como rodar

```
pip install -r requirements.txt
python LGPD.py
```

Obs.: o `psycopg2-binary` dessa versão não instala no Python 3.14. Use o Python 3.12 (`py -3.12 LGPD.py`).

## Arquivos

- `LGPD.py`: o programa.
- `requirements.txt`: bibliotecas usadas.
- Os arquivos `.csv` e o `tempos.log` são criados quando o programa roda.
