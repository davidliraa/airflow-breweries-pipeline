# Projeto BEES - Pipeline de Dados com Airflow e Arquitetura Medallion

## 📌 Visão Geral

Este projeto implementa uma pipeline de dados baseada em arquitetura **Medallion (Bronze, Silver e Gold)** utilizando **Apache Airflow** para orquestração, **Docker** para containerização e **Python/Pandas** para processamento de dados.

O objetivo é ingerir dados públicos da **API Open Brewery DB**, realizar transformações e gerar agregações para futuras análises.

---

## 🛠️ Arquitetura e Fluxo de Dados

- **Bronze:**  
Ingestão dos dados brutos da API. Arquivos salvos em formato **JSON** em `/data_lake/bronze/breweries`.

- **Silver:**  
Limpeza e transformação dos dados. Dados processados e exportados em formato **Parquet** particionado por estado em `/data_lake/silver/breweries`.

- **Gold:**  
Agregação dos dados (exemplo: **contagem de cervejarias por tipo e estado**). Resultado salvo em CSV na pasta `/data_lake/gold/breweries`.

---

## 🧰 Tecnologias e Ferramentas

- **Apache Airflow:** Orquestração das DAGs (Bronze → Silver → Gold)
- **Docker / Docker Compose:** Containerização do ambiente
- **Python 3.x + Pandas:** Transformação e manipulação dos dados
- **PostgreSQL:** Backend de metadata do Airflow

---

## 📂 Estrutura de Pastas

```
.
├── dags/
│   ├── bronze_ingest_breweries.py
│   ├── silver_transform_breweries.py
│   └── gold_aggregate_breweries.py
├── data_lake/
│   ├── bronze/breweries/
│   ├── silver/breweries/
│   └── gold/breweries/
├── docker-compose.yaml
├── .env
└── README.md
```

---

## ▶️ Como Executar

1. Configure o arquivo `.env` com os paths locais.
2. Suba os containers:  
   ```bash
   docker-compose up --build
   ```
3. Acesse a UI do Airflow:  
   [http://localhost:8080](http://localhost:8080)
4. Execute manualmente as DAGs na seguinte ordem:
   - **bronze_ingest_breweries**
   - **silver_transform_breweries**
   - **gold_aggregate_breweries**
5. Confira os arquivos gerados na pasta `/data_lake/gold/breweries`.

---

## ✅ Observações Finais

- Verifique o mapeamento correto de volumes para persistência de dados e logs.
- Todos os logs de execução estão disponíveis via Web UI do Airflow.
- O projeto foi validado ponta a ponta em ambiente local.

---

## 👤 Contato

**David Lira – Engenheiro de Dados**  
[LinkedIn](https://www.linkedin.com/in/david-a-lira/)
