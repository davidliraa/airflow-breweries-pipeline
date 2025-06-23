# BEES Project – Data Pipeline with Airflow and Medallion Architecture

## 📌 Overview

This project implements a data pipeline based on the **Medallion architecture (Bronze, Silver, and Gold layers)**, using **Apache Airflow** for orchestration, **Docker** for containerization, and **Python/Pandas** for data processing.

The goal is to ingest public data from the **Open Brewery DB API**, perform transformations, and generate aggregations for future analysis.

---

## 🛠️ Architecture and Data Flow

- **Bronze:**  
Raw data ingestion from the API. Files are saved in **JSON** format under `/data_lake/bronze/breweries`.

- **Silver:**  
Data cleaning and transformation. Processed data is exported in **partitioned Parquet** format by state to `/data_lake/silver/breweries`.

- **Gold:**  
Data aggregation (e.g., **brewery count by type and state**). Results are saved as CSV files in `/data_lake/gold/breweries`.

---

## 🧰 Technologies and Tools

- **Apache Airflow:** DAG orchestration (Bronze → Silver → Gold)
- **Docker / Docker Compose:** Environment containerization
- **Python 3.x + Pandas:** Data transformation and manipulation
- **PostgreSQL:** Airflow metadata backend

---

## 📂 Folder Structure

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

## ▶️ How to Run

1. Configure the `.env` file with your local paths.
2. Start the containers:  
   ```bash
   docker-compose up --build
   ```
3. Access the Airflow UI:  
   [http://localhost:8080](http://localhost:8080)
4. Manually run the DAGs in the following order:
   - **bronze_ingest_breweries**
   - **silver_transform_breweries**
   - **gold_aggregate_breweries**
5. Check the output files in `/data_lake/gold/breweries`.

---

## ✅ Final Notes

- Ensure correct volume mapping for data and log persistence.
- All execution logs are available via the Airflow Web UI.
- The project was fully validated end-to-end in a local environment.

---

## 👤 Contact

**David Lira – Data Engineer**  
[LinkedIn](https://www.linkedin.com/in/david-a-lira/)
