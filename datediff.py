import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def convert_datetype(df):
    df['conversion_date'] = pd.to_datetime(df['conversion_date'], format='%Y-%m-%d')
    df['activity_date'] = pd.to_datetime(df['activity_date'], format='%Y-%m-%d')
    return df

def calc_datediff(df):
    print("Caculating datediff...")
    for player in df.playerid.unique():
        datediff = (df[df.playerid == player]['conversion_date'] - df[df.playerid == player]['activity_date']).max().days
        ind = df[df.playerid == player].index
        df.loc[ind, 'datediff'] = int(datediff)
        # print(player, datediff, sep=': ')
    return df

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://root:"+"password"+"@localhost/abtest", encoding='utf-8')
    conn = engine.connect()

    df_A = pd.read_sql_query("SELECT * FROM purchased_group_A_total", con=conn, index_col='index')
    df_B = pd.read_sql_query("SELECT * FROM purchased_group_B_total", con=conn, index_col='index')
    
    df_A = calc_datediff(convert_datetype(df_A))
    df_B = calc_datediff(convert_datetype(df_B))
    df_A.to_sql(name="A_datediff", con=conn, if_exists='replace')
    df_B.to_sql(name="B_datediff", con=conn, if_exists='replace')

    