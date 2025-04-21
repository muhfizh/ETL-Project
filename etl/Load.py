import pymysql
import json

def load_to_mysql(df, config_path):
    with open(config_path) as f:
        config = json.load(f)
        
    print('Load Progress....')

    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        sql = """INSERT INTO penjualan (tanggal, produk, jumlah, harga, total) VALUES (%s, %s, %s, %s, %s)"""
        val = (row['Tanggal'], row['Produk'], row['Jumlah'], row['Harga'], row['Total'])
        cursor.execute(sql, val)

    conn.commit()
    cursor.close()
    conn.close()
    print('load Success')
