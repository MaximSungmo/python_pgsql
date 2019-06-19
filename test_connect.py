import psycopg2

try:
    conn = psycopg2.connect(
        user='webdb',
        password='webdb',
        host='192.168.1.49',
        port='5432',
        database='webdb')

    cursor = conn.cursor()
    cursor.execute('select version()')
    record = cursor.fetchone()
    print(f'connected to - {record}')



except Exception as e:
    print('error: {0}'.format(e))
finally:
    # conn이 살아 있으면 conn.close()
    'cursor' in locals() and cursor and cursor.close()
    'conn' in locals() and conn and conn.close()




