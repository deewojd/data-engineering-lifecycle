import duckdb

PARQUET_PATH = "/opt/spark/output/daily_sales_summary/*.parquet"

with duckdb.connect() as conn:
    print("Querying Parquet with DuckDB...")

    result = conn.execute("""
        SELECT
            order_date,
            product,
            total_quantity,
            total_revenue
        FROM read_parquet(?)
        ORDER BY order_date, product
    """, [PARQUET_PATH]).fetchdf()

    print("\nDaily sales summary:")
    print(result.to_string(index=False))

    print("\nRevenue by product:")
    revenue_by_product = conn.execute("""
        SELECT
            product,
            SUM(total_revenue) AS revenue
        FROM read_parquet(?)
        GROUP BY product
        ORDER BY revenue DESC
    """, [PARQUET_PATH]).fetchdf()

    print(revenue_by_product.to_string(index=False))
