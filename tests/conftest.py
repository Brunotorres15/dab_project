import sys
import os
import pytest

sys.path.append(os.getcwd())

# Returning a Spark Session
@pytest.fixture()
def spark():
    try: 
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
        print("Using Databricks Connect")
    except ImportError:
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
            print("Using PySpark")
        except ImportError:
            raise ImportError("Neither databricks.connect nor pyspark is available.")
    return spark