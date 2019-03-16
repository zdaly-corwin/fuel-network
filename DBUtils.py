__author__ = 'robert.corwin'

import numpy as np
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
from pandas import DataFrame

def get_db_conn():
    conn = create_engine('mysql+pymysql://Zdaly_Client:ClientPassword10$@fuelnetwork-cluster-db.cluster-coi1gninzesa.us-east-2.rds.amazonaws.com/FuelNetwork_DB')
    return conn

def run_qry(qry, conn):
    df = pd.read_sql_query(qry, conn)
    return df
