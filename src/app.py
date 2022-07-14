import psycopg2

conn = psycopg2.connect(database='database',
                        host='db',
                        user='user',
                        password='secret',
                        port='5432')
   