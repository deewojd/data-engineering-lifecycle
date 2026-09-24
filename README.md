# Data Engineering Lifecycle: Lean Stack

A small, reproducible data engineering pipeline built with **Python, Apache Airflow, Pandas, and DuckDB**.

This project explores how a lean technology stack can be used to build, orchestrate, and run a simple data pipeline locally in a containerized environment.

## Project Overview

The pipeline processes daily sales data from a CSV file, cleans and transforms the data, calculates revenue, aggregates sales by date and product, and stores the results in a DuckDB database.

**Pipeline flow:**

```text
CSV
 │
 ▼
Apache Airflow
 │
 ▼
Python + Pandas
 │
 ▼
DuckDB
```

## Technology Stack

| Technology     | Purpose                               |
| -------------- | ------------------------------------- |
| Python         | Data transformation logic             |
| Pandas         | Data cleaning and manipulation        |
| Apache Airflow | Pipeline orchestration and scheduling |
| DuckDB         | Local analytical data storage         |
| Docker         | Reproducible execution environment    |

## Pipeline

The pipeline performs the following steps:

1. Reads daily sales data from a CSV file.
2. Converts the order date into a date format.
3. Filters invalid records where:

   * Quantity is less than or equal to 0
   * Unit price is negative
4. Calculates revenue:

```text
revenue = quantity × unit_price
```

5. Aggregates sales by:

   * Order date
   * Product
6. Calculates:

   * Total quantity
   * Total revenue
7. Writes the resulting table to DuckDB.

## Example Input

The pipeline uses sales data with the following structure:

```text
order_id
order_date
product
quantity
unit_price
```

Example:

```csv
order_id,order_date,product,quantity,unit_price
1001,2026-09-01,Notebook,2,12.00
1002,2026-09-01,Pen,5,2.50
1003,2026-09-01,Notebook,1,12.00
```

## Example Output

The pipeline produces a `daily_sales_summary` table containing:

| order_date | product  | total_quantity | total_revenue |
| ---------- | -------- | -------------: | ------------: |
| 2026-09-01 | Notebook |              3 |         36.00 |
| 2026-09-01 | Pen      |              5 |         12.50 |
| 2026-09-02 | Backpack |              1 |         45.00 |
| 2026-09-02 | Notebook |              2 |         24.00 |
| 2026-09-02 | Pen      |              3 |          7.50 |

## Airflow Orchestration

Apache Airflow schedules and runs the transformation pipeline.

The DAG:

```text
daily_sales_pipeline
        │
        ▼
run_sales_pipeline
        │
        ▼
transform_sales.py
```

The DAG is configured to run daily and uses Docker to provide a consistent execution environment.

## Project Structure

```text
lean-stack/
├── .gitignore
├── Dockerfile
├── docker-compose.yaml
├── dags/
│   └── daily_sales_dag.py
├── data/
│   └── daily_sales.csv
├── scripts/
│   └── transform_sales.py
└── warehouse/
    └── sales.duckdb  # generated locally when the pipeline runs
```

The DuckDB database and Airflow-generated files are excluded from Git because they are created locally when the pipeline runs.

## Running the Pipeline

### 1. Clone the repository

```bash
git clone https://github.com/deewojd/data-engineering-lifecycle.git
cd data-engineering-lifecycle/lean-stack
```

### 2. Start Airflow

```bash
docker compose up -d
```

### 3. Open Airflow

Open:

```text
http://localhost:8080
```

The local Airflow environment uses the default development credentials configured during setup.

### 4. Run the DAG

From the Airflow UI, locate:

```text
daily_sales_pipeline
```

and trigger a run.

The DAG executes the Python transformation and writes the resulting data to DuckDB.

### 5. Stop the environment

```bash
docker compose down
```

## Why This Stack?

The goal of this implementation is to demonstrate how a relatively small data pipeline can be built using a **lean technology stack**.

Each component has a focused responsibility:

* **Python/Pandas** handles transformation logic.
* **Airflow** handles orchestration and scheduling.
* **DuckDB** provides local analytical storage.
* **Docker** creates a reproducible environment.

This approach keeps the architecture relatively simple while still demonstrating important data engineering concepts such as **orchestration, transformation, data quality filtering, analytical storage, containerization, and reproducibility**.

## Key Takeaways

This implementation demonstrates:

* Building a batch data pipeline
* Separating transformation logic from orchestration
* Scheduling workflows with Apache Airflow
* Performing data cleaning and aggregation with Pandas
* Writing analytical results to DuckDB
* Containerizing a data engineering environment with Docker
* Creating a reproducible local development setup

## Project Status

**Lean Stack: Complete**

Future versions of this project will implement the same pipeline using additional technologies to compare how different technology choices affect development, operations, scalability, and ownership across the data engineering lifecycle.
