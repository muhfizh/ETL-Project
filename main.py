from etl.Extract import extract_excel, extract_csv
from etl.Transfrom import transform_data
from etl.Load import load_to_mysql

# excel
dfexcel = extract_excel("data/penjualan.xlsx")
df_clean_excel = transform_data(dfexcel)
load_to_mysql(df_clean_excel, "config/db_config.json")

# csv
dfcsv = extract_csv("data/penjualan.csv")
df_clean_csv = transform_data(dfcsv)
load_to_mysql(df_clean_csv, "config/db_config.json")