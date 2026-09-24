from pathlib import Path

import duckdb
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "daily_sales.csv"
DATABASE_FILE = PROJECT_ROOT / "warehouse" / "sales.duckdb"

def main():
    print("Reading sales data...")
    
    # Read source data
    df = pd.read_csv(INPUT_FILE)

    print(f"Rows read: {len(df)}")

    # Convert order_date to dt
    df["order_date"] = pd.to_datetime(df["order_date"]).dt.date

    # Remove invalid records
    df = df[
        (df["quantity"] > 0)
        & (df["unit_price"] >= 0)
    ].copy()

    # Calculate revenue
    df["revenue"] = df["quantity"] * df["unit_price"]

    # Aggregate sales
    summary = (
        df.groupby(["order_date", "product"], as_index=False)
        .agg(
            total_quantity=("quantity","sum"),
            total_revenue=("revenue", "sum"),
        )
    )
        
    # Writing the result to DuckDB
    DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with duckdb.connect(str(DATABASE_FILE)) as conn:
        conn.execute("DROP TABLE IF EXISTS daily_sales_summary")

        conn.register("sales_summary", summary)

        conn.execute("""
            CREATE TABLE daily_sales_summary AS
            SELECT *
            FROM sales_summary
            ORDER BY order_date, product
        """)

    print("Pipeline completed successfully.")
    print(f"Output database: {DATABASE_FILE}")
    print(summary.to_string(index=False))

if __name__ == "__main__":
        main()
