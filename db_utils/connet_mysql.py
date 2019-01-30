import mysql.connector
from db_utils.db_config import MYSQL

def connect(db=MYSQL):
    cnx = mysql.connector.connect(**db)
    cursor = cnx.cursor(buffered=True)
    # test_sql = "SELECT property_id FROM property_list;"
    # cursor.execute(test_sql)
    # for i in cursor:
    #     print(i)
    print("Before function: ", cursor)
    return cursor

if __name__ == '__main__':
    test_sql = "SELECT * FROM purchased_group_B_total;"

    cursor = connect()
    print("After function: ", cursor)
    cursor.execute(test_sql)
    for i in cursor:
        print(i)