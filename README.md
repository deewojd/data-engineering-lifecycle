# Data Engineering Lifecycle: Choosing Technologies

A hands-on data engineering project exploring how technology choices affect the design, development, and operation of a data pipeline.

Inspired by Chapter 4, **“Choosing Technologies Across the Data Engineering Lifecycle,”** from *Fundamentals of Data Engineering*.

The project implements the same small daily sales pipeline using three different technology approaches:

1. **Lean Stack:** Python, Pandas, DuckDB, and Apache Airflow
2. **Self-Managed Spark:** PySpark, Spark Standalone, Parquet, DuckDB, and Apache Airflow
3. **Databricks:** Spark, Delta Lake, Databricks SQL, and Databricks Workflows

The goal is to understand how workload characteristics, team expertise, scalability, governance, operational ownership, and managed services influence technology selection.

---

## Project Overview

The pipeline processes daily sales data by:

* Reading sales records from CSV
* Validating and cleaning the data
* Calculating revenue
* Aggregating sales by date and product
* Persisting the analytical output
* Querying the resulting data with SQL

The business logic is intentionally kept consistent across implementations so that the technology choices can be compared more directly.

### Input

A small daily sales CSV containing:

* Order date
* Product
* Quantity
* Unit price

### Transformation

```text
quantity > 0
unit_price >= 0
revenue = quantity × unit_price
```

The pipeline then aggregates:

```text
order_date + product
        ↓
total_quantity
total_revenue
```

---

## Architecture

### 1. Lean Stack

```text
CSV
 ↓
Apache Airflow
 ↓
Python + Pandas
 ↓
DuckDB
 ↓
SQL
```

**Technologies**

* Python
* Pandas
* Apache Airflow
* DuckDB
* Docker

**Purpose**

This implementation represents a relatively lightweight architecture for a small analytical workload.

[Explore the Lean Stack](./lean-stack/)

---

### 2. Self-Managed Spark

```text
CSV
 ↓
Apache Airflow
 ↓
spark-submit
 ↓
Spark Standalone
 ├── Worker 1
 └── Worker 2
 ↓
PySpark
 ↓
Parquet
 ↓
DuckDB
 ↓
SQL
```

**Technologies**

* PySpark
* Apache Spark
* Spark Standalone
* Apache Airflow
* Parquet
* DuckDB
* Docker

**Purpose**

This implementation explores what changes when the processing layer moves from a lightweight Python workflow to distributed Spark while the infrastructure and cluster management remain under the team's responsibility.

[Explore the Self-Managed Spark implementation](./self-managed-spark/)

---

### 3. Databricks

```text
CSV
 ↓
Databricks Workflows
 ↓
Apache Spark
 ↓
Delta Lake
 ↓
Databricks SQL
```

**Technologies**

* Databricks
* Apache Spark
* Delta Lake
* Databricks Workflows
* Databricks SQL

**Purpose**

This implementation explores a managed data platform where infrastructure and much of the operational complexity are delegated to the platform.

[Explore the Databricks implementation](./databricks/)

---

## Technology Comparison

| Implementation     | Processing      | Storage / Query Layer       | Orchestration / Cluster Management | Environment   |
| ------------------ | --------------- | --------------------------- | ---------------------------------- | ------------- |
| Lean Stack         | Python + Pandas | DuckDB                      | Apache Airflow                     | Local Docker  |
| Self-Managed Spark | PySpark         | Parquet + DuckDB            | Apache Airflow + Spark Standalone  | Local Docker  |
| Databricks         | Spark           | Delta Lake + Databricks SQL | Databricks Workflows               | Managed Cloud |

---

## What Stays the Same

To make the comparison clear, the core business logic remains consistent across implementations.

Each pipeline:

1. Reads the same sales data
2. Applies the same validation rules
3. Calculates revenue
4. Groups by date and product
5. Produces the same analytical result
6. Supports SQL-based analysis

This allows the project to focus on the impact of **technology and architecture choices**, rather than differences in business requirements.

---

## What Changes

The implementations differ primarily in how the pipeline handles:

### Processing

* Python/Pandas
* Distributed PySpark
* Managed Spark

### Storage

* DuckDB database
* Parquet files
* Delta Lake

### Orchestration

* Airflow
* Airflow 
* Databricks Workflows

### Operational Ownership

The project also demonstrates a progression from:

```text
More infrastructure managed by the team
                ↓
        Self-managed Spark
                ↓
     More platform-managed services
                ↓
            Databricks
```

This illustrates an important data engineering tradeoff: choosing technologies is not only about processing capability. It also involves operational responsibility, team expertise, governance, scalability, and the amount of infrastructure a team wants to manage itself.

---

## Results

The first two implementations produce the same analytical results from the shared input dataset.

### Revenue by Product

| Product  | Revenue |
| -------- | ------: |
| Notebook |  $60.00 |
| Backpack |  $45.00 |
| Pen      |  $20.00 |

The Self-Managed Spark implementation successfully runs the pipeline through:

```text
Airflow
 → spark-submit
 → Spark Standalone
 → PySpark
 → Parquet
 → DuckDB
```

The Databricks implementation will be evaluated using the same business logic and output expectations.

---

## Key Data Engineering Concepts Demonstrated

* Data pipeline design
* Workflow orchestration
* Batch processing
* Distributed processing with Spark
* Spark cluster management
* PySpark
* Columnar storage with Parquet
* Analytical SQL
* DuckDB
* Managed data platforms
* Delta Lake
* Technology selection
* Operational ownership
* Scalability considerations
* Reproducible local environments with Docker
* Git-based project organization

---

## Project Structure

```text
data-engineering-lifecycle/
│
├── lean-stack/
│   ├── dags/
│   ├── data/
│   ├── scripts/
│   ├── warehouse/
│   ├── Dockerfile
│   └── docker-compose.yaml
│
├── self-managed-spark/
│   ├── airflow/
│   │   ├── dags/
│   │   └── Dockerfile
│   ├── data/
│   ├── scripts/
│   ├── output/
│   ├── Dockerfile
│   └── docker-compose.yaml
│
└── databricks/ 
```

---

## Status

| Implementation     | Status      |
| ------------------ | ----------- |
| Lean Stack         | Complete    |
| Self-Managed Spark | Complete    |
| Databricks         | In progress |

---

## References

* *Fundamentals of Data Engineering:* Joe Reis and Matt Housley
* Apache Airflow documentation
* Apache Spark documentation
* DuckDB documentation
* Databricks documentation
