from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("House Prices Analysis") \
    .getOrCreate()

# Загрузка данных из PostgreSQL
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/mydb") \
    .option("dbtable", "house_prices") \
    .option("user", "myuser") \
    .option("password", "mypassword") \
    .load()

# Выполнение анализа данных
result = df.groupBy("район", "количество_комнат") \
    .avg("стоимость") \
    .orderBy("район", "количество_комнат")

# Вывод результатов
result.show()
