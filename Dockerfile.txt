FROM bitnami/spark
COPY init.sql /docker-entrypoint-initdb.d/
COPY house_prices.csv /house_prices.csv
COPY postgresql-42.7.0.jar /opt/bitnami/spark/jars/
COPY my_spark.py /bin/my_spark.py
