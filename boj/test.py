from pyspark.sql.functions import to_timestamp

sc=spark.data
(sc
    .parallelize([Row(dt='2016_08_21 11_31_08')])
    .toDF()
    .withColumn("parsed", to_timestamp("dt", "yyyy_MM_dd HH_mm_ss"))
    .show(1, False))