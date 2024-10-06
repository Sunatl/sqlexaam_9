import psycopg2
conn = psycopg2.connect(
    database = 'main_dbss'
    user  = 'postgres',
    host  = 'localhost',
    password = '0874326951',
    port  = '5432'    
)
cur = conn.cursor()
cur.execute()