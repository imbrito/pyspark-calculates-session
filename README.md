# Calculates Session

Solução para o `Data Engineer Challenge` disponível em: https://grupozap.github.io/squad-data-platform/data-engineer-test.

## Estrutura do Repositório

```
    ├── calculates_session.py
    ├── LICENSE
    ├── Makefile
    ├── README.md
    └── requirements.txt
```

## Setup

Para correta execução instale as dependências abaixo:

- `Python: 3.7+`
- `Virtualenv: 16.4.3+`
- `Wget: 1.17.1+`

1. clone o repositório: `$ git clone git@github.com:imbrito/grupozap.git`.
2. acesse a pasta do projeto: `$ cd grupozap`.
3. execute: `$ make install`. Serão executadas as seguintes ações:
    - será iniciado o donwload dos arquivos que serão usados durante a solução
    - será criado um ambiente de desenvolvimento virtual para `python`
    - serão instaladas as dependências de execução do pipeline

A estrutura do projeto, após a execução do comando: `$ make install`. 

```
    ├── calculates_session.py
    ├── data
    │   ├── part-00000.json.gz
    │   ├── part-00001.json.gz
    │   ├── part-00002.json.gz
    │   ├── part-00003.json.gz
    │   └── part-00004.json.gz
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    └── venv
```

## Executando o pipeline

- acesse a pasta do projeto: `$ cd grupozap`.
- ative o ambiente virtual: `$ source venv/bin/activate`.

O pipeline consiste na execução de um `script` baseado em `PySpark`, API Python para o Apache Spark. Acesse a documentação, 
através de: https://spark.apache.org/docs/latest/api/python/pyspark.sql.html.

### Opções de execução

TODO