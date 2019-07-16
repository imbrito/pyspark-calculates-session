#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession, Window
from pyspark.sql import functions as F
from pyspark.sql.types import StructField, StructType, StringType, LongType
from datetime import datetime
import argparse, os

PWD = os.getenv("PWD")

def schema():
    return StructType([StructField("anonymous_id", StringType(), True),
                       StructField("device_sent_timestamp", LongType(), True),
                       StructField("name", StringType(), True),
                       StructField("browser_family", StringType(), True),
                       StructField("os_family", StringType(), True),
                       StructField("device_family", StringType(), True),])


def format_logger(level="INFO"):
    return {"datetime": datetime.now().strftime("%y/%m/%d %H:%M:%S"), "level": level}


def check_positive(value):
    arg = int(value)
    if arg <= 0: 
        raise argparse.ArgumentTypeError("{} is an invalid positive integer value.".format(value))
    return arg


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--browser", help="show sessions only: browser_family.", action="store_true")
    parser.add_argument("-o", "--os", help="show sessions only: os_family.", action="store_true")
    parser.add_argument("-d", "--device", help="show sessions only: device_family.", action="store_true")
    parser.add_argument("-a", "--all", help="show sessions by: browser_family, os_family and device_family.", action="store_true")
    parser.add_argument("-t", "--table", help="show sessions in table format.", action="store_true")
    parser.add_argument("-w", "--write", help="saves the content in JSON format.", action="store_true")
    parser.add_argument("-f", "--files", type=int, choices=[1,2,3,4,5], default=1, help="number of files to calculates session.")
    parser.add_argument("-s", "--show", type=check_positive, default=5, help="number of rows show by exibition.")
    return parser.parse_args()


def sessions_by_column(df, column, args):
    print("{datetime} {level} calculates sessions by: {column}.".format(column=column, **format_logger()))
    sessions = df.groupBy(column) \
                 .agg(F.count(df.anonymous_id).alias("sessions")) \
                 .orderBy("sessions", ascending=False)
        
    row = sessions.agg(F.collect_set(column).alias(column)).first()
    cols = sorted(list(map(lambda attr: attr, row.__getattr__(column))))

    sessions = sessions.withColumn("type", F.lit(column))
    pivot = sessions.groupBy("type").pivot(column, cols).max("sessions") 
    
    if args.table:
        print("{datetime} {level} show sessions by: {column} in table format.".format(column=column, **format_logger()))
        sessions.drop("type").show(args.show, truncate=False)
    
    print("{datetime} {level} show sessions by: {column} in JSON format.".format(column=column, **format_logger()))
    to_json = pivot.drop("type").toJSON().first()
    print("{} \n".format(to_json))

    if args.write:
        print("{datetime} {level} write sessions by: {column} in JSON format.".format(column=column, **format_logger()))
        pivot.drop("type").coalesce(1).write.json(path="{pwd}/results/{column}".format(pwd=PWD,column=column),mode="overwrite",compression="gzip")


if __name__ == "__main__":

    try:    
        args = read_args()  
        data = [ "{pwd}/data/part-0000{x}.json.gz".format(pwd=PWD, x=y) for y in range(args.files) ]

        print("{datetime} {level} build a new instance.".format(**format_logger()))
        spark = SparkSession.builder \
                            .appName("Test Spark") \
                            .getOrCreate()

        print("{datetime} {level} read data: {data}.".format(data=data, **format_logger()))
        df = spark.read.json(path=data, schema=schema())
        print("{datetime} {level} rows count: {rows}.".format(rows=df.count(), **format_logger()))
        
        # -1800 seconds = -60 seconds * 30 minutes
        w = Window.partitionBy("anonymous_id").orderBy("device_sent_timestamp").rangeBetween(start=-1800, end=0)
        
        # add column events_on_session, based on window spec
        df = df.withColumn("events_on_session", F.count(df.device_sent_timestamp).over(w))
        
        # add column event_time, based on column device_sent_timestamp
        df = df.withColumn("event_time", F.to_timestamp(df.device_sent_timestamp))
        
        # filter df by first event on session
        df = df.filter(df.events_on_session == 1)
        print("{datetime} {level} distinct sessions: {rows}.".format(rows=df.count(), **format_logger()))

        if args.all or args.browser:
            sessions_by_column(df, "browser_family", args)
            
        if args.all or args.os:
            sessions_by_column(df, "os_family", args)

        if args.all or args.device:
            sessions_by_column(df, "device_family", args)
        
        print("{datetime} {level} finished.".format(**format_logger()))

    except Exception as e:
        print("{datetime} {level} failed: {msg}.".format(**format_logger("ERROR"), msg=str(e)))