__author__ = 'robert.corwin'

import numpy as np
import pandas as pd
from pandas import DataFrame
from DBUtils import *

conn = get_db_conn()
qry = "select * from SiteAttributes_Current"
df = run_qry(qry, conn)

debug = True
