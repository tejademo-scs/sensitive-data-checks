import os
from influxdb import InfluxDBClient

def set_jenkins_connection():
    client = None
    username = os.environ["INFLUXDB_USERNAME"]
    influxdb = os.environ["INFLUXDB_PASSWORD"]

    print("INFLUXDB_USERNAME: %s" % username)
    print("INFLUXDB_PASSWORD: %s" % influxdb)

    client = InfluxDBClient(
        host='metricsdb.sgpoolz.com.sg',
        port=8086,
        username=username,
        password=influxdb,
        database='aws_applications'
    )

    return client

# Example usage
if __name__ == "__main__":
    db_client = set_jenkins_connection()
    print("InfluxDB client initialized.")
