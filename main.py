import psycopg2
import os
import pandas as pd

def main():
	# con = psycopg2.connect(os.environ.get("POSTGRES_URI"))
    con = psycopg2.connect('postgres://hnewxezrserycc:fa7730d9660660f7dc0292e1282e327c0a93ff49d062cf25f270d30bc27747e3@ec2-3-209-61-239.compute-1.amazonaws.com:5432/d26q7d7nbt04qe')
    cur = con.cursor()
    select_all_query = """SELECT * FROM playlists"""
    # for if i wanted all 
    # cur.execute(select_all_query)
    # query_results = cur.fetchall()
    def create_pandas_table(sql_query, database = con):
        table = pd.read_sql_query(sql_query, database)
        return table

    playlist_table = create_pandas_table(select_all_query)
    print(playlist_table)
    cur.close()
    con.close()


if __name__=="__main__":
    main()