def transform_data(df):
    df = df.dropna()
    df['Total'] = df['Jumlah'] * df['Harga']
    print('Transform Running')
    return df