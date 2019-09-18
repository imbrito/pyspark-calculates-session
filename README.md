# Calculates Session

Solução para o desafio proposto, em: [Data Engineer Challenge](CHALLENGE.md).

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

1. clone o repositório: `$ git clone git@github.com:imbrito/pyspark-calculates-session.git`.
2. acesse a pasta do projeto: `$ cd pyspark-calculates-session`.
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

- acesse a pasta do projeto: `$ cd pyspark-calculates-session`.
- ative o ambiente virtual: `$ source venv/bin/activate`.

O pipeline consiste na execução de um `script` baseado em `PySpark`, API Python para o Apache Spark. Acesse a documentação, 
através de: https://spark.apache.org/docs/latest/api/python/pyspark.sql.html.

### Opções de execução

Para saber as opções disponíveis: `$ python calculates_session.py -h`

```
usage: calculates_session.py [-h] [-b] [-o] [-d] [-a] [-t] [-w]
                             [-f {1,2,3,4,5}] [-s SHOW]
```

Argumentos Opicionais:

|    argument   | type | default |   choices   | description                                                   |
|---------------|------|---------|-------------|---------------------------------------------------------------|
| -h, --help    | bool |  False  |     n/a     | show this help message and exit                               |
| -b, --browser | bool |  False  |     n/a     | show sessions only: browser_family                            |
| -o, --os      | bool |  False  |     n/a     | show sessions only: os_family                                 |
| -d, --device  | bool |  False  |     n/a     | show sessions only: device_family                             |
| -a, --all     | bool |  False  |     n/a     | show sessions by: browser_family, os_family and device_family |
| -t, --table   | bool |  False  |     n/a     | show sessions in table format                                 |
| -w, --write   | bool |  False  |     n/a     | saves the content in JSON format                              |
| -f, --fles    | int  |    1    | {1,2,3,4,5} | number of files to calculates session                         |
| -s, --show    | int  |    5    |   int > 0   | number of rows show by exibition                              |

### Exemplos 

- Calcular apenas sessões para `browser_family` usando apenas 1 arquivo: `$ python calculates_session.py -b`

1. sessions by: browser_family in JSON format (exemplo com 10 regitros aleatórios)

```JSON
{
   "Chrome Mobile":326714,
   "Chrome":295874,
   "Mobile Safari":79196,
   "Other":63887,
   "Firefox":23335,
   "Facebook":18085,
   "Edge":10291,
   "Chrome Mobile iOS":8574,
   "Safari":6346,
   "IE":4586
}
```

- Calcular apenas sessões para `os_family` usando apenas 2 arquivos e exibindo o resultado como `JSON` e `table` com 10 `rows`: 
`$ python calculates_session.py -o -t -s 10 -f 2`

1. sessions by: os_family in table format
                                                          
|os_family  |sessions|
|-----------|--------|
|Android    |706744  |
|Windows 10 |310517  |
|Windows 7  |260436  |
|iOS        |179824  |
|Other      |129152  |
|Windows 8.1|45097   |
|Mac OS X   |33835   |
|Windows 8  |6820    |
|Windows XP |6561    |
|Linux      |5975    |

only showing top 10 rows

2. sessions by: os_family in JSON format (exemplo com 10 regitros aleatórios)

```JSON
{
   "Android":706744,
   "Windows 10":310517,
   "Windows 7":260436,
   "iOS":179824,
   "Other":129152,
   "Windows 8.1":45097,
   "Mac OS X":33835,
   "Windows 8":6820,
   "Windows XP":6561,
   "Linux":5975
} 
```

- Calcular apenas sessões para `device_family` usando apenas 1 arquivo e salvando o resultado como `JSON`: 
`$ python calculates_session.py -d -w`

1. sessions by: device_family in JSON format (exemplo com 10 regitros aleatórios)

```JSON
{
   "Other":399092,
   "Generic Smartphone":248395,
   "iPhone":80719,
   "iPad":7556,
   "LG-M250":6147,
   "Samsung SM-G610M":4403,
   "LG-K430":4319,
   "Nexus 5":4139,
   "Samsung SM-J500M":3687,
   "Samsung SM-G570M":3343
} 
```

2. estrutura do projeto após salvar o resultado como `JSON`

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
    ├── results
    │   └── device_family
    │       ├── part-00000-<hash>.json.gz
    │       └── _SUCCESS
    └── venv
```

Experimente outras opções:

- Calcular sessões para `browser_family`, `os_family` e `device_family` usando todos os arquivos e salvar os resultados 
como `JSON`: `$ python calculates_session.py -a -w -f 5`

- Calcular sessões para `browser_family`, `os_family` e `device_family` usando todos os arquivos e exibir os resultados 
como `JSON` e `table`: `$ python calculates_session.py -a -t -f 5`
