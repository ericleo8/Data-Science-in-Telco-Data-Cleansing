#import library
import pandas as pd
pd.options.display.max_columns = 50

#import dataset
df_load = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')

# Tampilkan jumlah baris dan kolom
print(df_load.shape)

# Tampilkan 5 data teratas
print(df_load.head(5))

# Jumlah ID yang unik
print(df_load.customerID.nunique())

###Mencari Validitas ID Pelanggan###
df_load = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')

df_load['valid_id'] = df_load['customerID'].astype(
    str).str.match(r'(45\d{9,10})')
df_load = (df_load[df_load['valid_id'] == True]).drop('valid_id', axis=1)
print('Hasil jumlah ID Customer yang terfilter adalah',
      df_load['customerID'].count())

# Drop Duplicate Rows
df_load.drop_duplicates()
# Drop duplicate ID sorted by Periode
df_load = df_load.sort_values(
    'UpdatedAt', ascending=False).drop_duplicates('customerID')
print('Hasil jumlah ID Customer yang sudah dihilangkan duplikasinya (distinct) adalah',
      df_load['customerID'].count())
