from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

spark = (
    SparkSession.builder
    .appName("DailySalesPipeline")
    .getOrCreate()
)

input_file = "/opt/spark/data/daily_sales.csv"
output_path = "/opt/spark/output/daily_sales_summary"

print("Reading sales data...")

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(input_file)
)

print(f"Rows read: {df.count()}")

df = (
    df
    .withColumn("order_date", col("order_date").cast("date"))
    .filter(
        (col("quantity") > 0)
        & (col("unit_price") >= 0)
    )
    .withColumn(
        "revenue",
        col("quantity") * col("unit_price")
    )
)

summary = (
    df.groupBy("order_date", "product")
    .agg(
        sum("quantity").alias("total_quantity"),
        sum("revenue").alias("total_revenue"),
    )
    .orderBy("order_date", "product")
)

print("Daily sales summary:")
summary.show()

summary.write.mode("overwrite").parquet(output_path)

print(f"Output written to: {output_path}")

spark.stop()
