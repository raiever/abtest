import pandas as pd
from google.cloud import bigquery

from db_utils import connet_mysql
from sqlalchemy import create_engine

client = bigquery.Client(project=)

engine = create_engine("mysql+mysqldb://root:"+"password"+"@localhost/abtest", encoding='utf-8')
conn = engine.connect()

sql = """
SELECT
*
FROM `.abtest.join_real_%s`
WHERE conversion_date IS NOT NULL 
"""

funnel_A = client.query(sql %'A').to_dataframe()
funnel_B = client.query(sql %'B').to_dataframe()

cursor = connet_mysql.connect()

funnel_A.to_sql(name='purchased_group_A_total', con=engine, if_exists='replace')
funnel_B.to_sql(name='purchased_group_B_total', con=engine, if_exists='replace')