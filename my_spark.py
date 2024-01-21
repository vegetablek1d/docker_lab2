from pyspark.sql import SparkSession

# Создание сессии Spark
spark = SparkSession.builder \
    .appName("Data Processing") \
    .getOrCreate()

# Подключение к БД PostgreSQL
jdbc_url = "jdbc:postgresql://postgres:5432/mydatabase"
connection_properties = {
    "user": "user",
    "password": "pass_123",
    "driver": "org.postgresql.Driver"
}

# Загрузка данных из таблиц БД
df_googleplaystore = spark.read \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "googleplaystore") \
    .option("properties", connection_properties) \
    .load()

df_googleplaystore_user_reviews = spark.read \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "googleplaystore_user_reviews") \
    .option("properties", connection_properties) \
    .load()

# Обработка данных и вывод результатов
df_result = df_googleplaystore \
    .join(df_googleplaystore_user_reviews, "category") \
    .groupBy("category") \
    .agg(
        sum("positive_reviews").alias("total_positive_reviews"),
        sum("negative_reviews").alias("total_negative_reviews")
    )

df_result.show()