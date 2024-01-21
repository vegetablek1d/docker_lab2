from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Создание Spark сессии
spark = SparkSession.builder \
    .appName("HousePricesAnalysis") \
    .config("spark.driver.extraClassPath", "/opt/bitnami/spark/jars/postgresql-42.7.0.jar") \
    .getOrCreate()

# Загрузка данных из PostgreSQL таблицы
jdbc_url = "jdbc:postgresql://postgres:5432/mydb"
connection_properties = {
    "user": "myuser",
    "password": "mypassword",
    "driver": "org.postgresql.Driver"
}

house_prices_df = spark.read \
    .jdbc(url=jdbc_url, table="house_prices", properties=connection_properties)

# Выполнение анализа данных
result_df = house_prices_df.groupBy("location", "bedrooms") \
    .agg(avg("price").alias("avg_price")) \
    .orderBy("location", "bedrooms")

# Вывод результатов
result_df.show()

# Завершение Spark сессии
spark.stop()
