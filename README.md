# Projeto BEES - Open Brewery DB - Pipeline Medallion

## Visão Geral

Este projeto implementa uma pipeline de dados em arquitetura medallion (Bronze, Silver e Gold) utilizando Apache Airflow para orquestração, Docker para containerização e Python/Pandas para transformação dos dados. O objetivo é ingerir dados públicos da API Open Brewery DB, tratar e agregar informações para análises futuras.

---

## Arquitetura e Fluxo de Dados

- **Bronze:** Ingestão dos dados brutos da API Open Brewery DB. Os dados são salvos em formato JSON na pasta `/data_lake/bronze/breweries`.
- **Silver:** Transformação e limpeza dos dados brutos. Os arquivos JSON são carregados, colunas desnecessárias são removidas e os dados são salvos em CSV na pasta `/data_lake/silver/breweries`.
- **Gold:** Agregação dos dados transformados para gerar insights. Neste caso, a contagem de cervejarias por estado, armazenada em CSV na pasta `/data_lake/gold/breweries`.

---

## Tecnologias e Ferramentas

- Apache Airflow: Orquestração dos pipelines (DAGs bronze, silver, gold)
- Docker/Docker Compose: Containerização e ambiente isolado
- Python 3.x: Programação das tarefas e transformação dos dados
- Pandas: Manipulação e transformação dos dados tabulares
- PostgreSQL: Banco de dados usado pelo Airflow para backend metadata

---

## Estrutura de Pastas

.
├── dags/
│ ├── bronze_ingest_breweries.py
│ ├── silver_transform_breweries.py
│ └── gold_aggregate_breweries.py
├── data_lake/
│ ├── bronze/breweries/
│ ├── silver/breweries/
│ └── gold/breweries/
├── docker-compose.yaml
├── .env
└── README.md


---

## Como Executar

1. Configure o arquivo `.env` com as variáveis de ambiente necessárias.
2. Execute `docker-compose up --build` para subir os containers do Airflow.
3. Acesse o Airflow Webserver via `http://localhost:8080`.
4. Execute manualmente as DAGs na ordem: **bronze_ingest_breweries → silver_transform_breweries → gold_aggregate_breweries**.
5. Os arquivos processados estarão disponíveis em `/data_lake/gold/breweries`.

---

## Observações

- Garanta que as pastas mapeadas no Docker estão corretas para persistência dos dados e logs.
- Os logs das tarefas podem ser acessados diretamente pela interface web do Airflow.
- Recomenda-se executar as DAGs manualmente na primeira vez para validar o fluxo e os dados.

---

## Contato

David Lira - Engenheiro de Dados  
LinkedIn: https://www.linkedin.com/in/david-a-lira/
