from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder \
    .appName("(Не)движимость") \
    .config("spark.driver.extraClassPath", "/opt/bitnami/spark/jars/postgresql-42.7.0.jar") \
    .getOrCreate()

jdbc_url = "jdbc:postgresql://postgres:5432/houses"
connection_properties = {
    "user": "user",
    "password": "password",
    "driver": "org.postgresql.Driver"
}

df = spark.read.option("header", "true").csv("/opt/bitnami/spark/house_prices.csv")

print(df)


result_df = df.groupBy("location", "bedrooms") \
    .agg(avg("price").alias("avg_price")) \
    .orderBy("location", "bedrooms")

result_df.show()

spark.stop()
