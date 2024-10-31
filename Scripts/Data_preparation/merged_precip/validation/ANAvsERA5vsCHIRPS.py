import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load and preprocess ANA data
df_ANA = pd.read_csv(r'G:\My Drive\Doutorado\TESE\2. Artigo 2\Artigo Pantanal - LULCC\Codes\pantanal-lc\2024_reviews\merged_precip\validation\selected_stations_data.csv')
df_ANA['date'] = pd.to_datetime(df_ANA['date'])
df_ANA['year'] = df_ANA['date'].dt.year
df_ANA['month'] = df_ANA['date'].dt.month

# Group by year and month, summing only numeric columns
df_ANA = df_ANA.groupby(['year', 'month']).sum(numeric_only=True).reset_index()
df_ANA['Date'] = pd.to_datetime(df_ANA['year'].astype(str) + '-' + df_ANA['month'].astype(str), format='%Y-%m')

# Load and preprocess ERA5 data
df_ERA5 = pd.read_csv(r'G:\My Drive\Doutorado\TESE\2. Artigo 2\Artigo Pantanal - LULCC\Codes\pantanal-lc\2024_reviews\merged_precip\validation\ERA5_precip_stations_all.csv')
code_columns = ['1456001', '1456003', '1456009', '1457000', '1457001', '1554006', '1556000',
                '1556001', '1556002', '1556006', '1557001', '1557003', '1558000', '1558001',
                '1558004', '1558005', '1654000', '1654001', '1655000', '1655001', '1655002',
                '1655004', '1656001', '1656002', '1656003', '1656004', '1657000', '1657002',
                '1657003', '1657004', '1658000', '1754000', '1754002', '1754004', '1755003',
                '1756000', '1756001', '1756003', '1757001', '1853000', '1853002', '1854001',
                '1854002', '1854003', '1854004', '1857001', '1857003', '1954002', '1954003',
                '1954004', '1956003', '1956004', '1956005', '1957000', '1957003', '1957004',
                '1957005', '1957006', '2054000', '2054005', '2055000', '2055001', '2055002',
                '2056001', '2056003', '2056005', '2155001', '2156000', '2156001', '2157003',
                '2157004', '2256001', '2257000']
df_ERA5[code_columns] = df_ERA5[code_columns] * 1000
df_ERA5['Date'] = pd.to_datetime(df_ERA5['year'].astype(str) + '-' + df_ERA5['month'].astype(str), format='%Y-%m')

# Load and preprocess CHIRPS data
df_CHIRPS = pd.read_csv(r'G:\My Drive\Doutorado\TESE\2. Artigo 2\Artigo Pantanal - LULCC\Codes\pantanal-lc\2024_reviews\merged_precip\validation\CHIRPS_precip_stations_all.csv')
df_CHIRPS['Date'] = pd.to_datetime(df_CHIRPS['year'].astype(str) + '-' + df_CHIRPS['month'].astype(str), format='%Y-%m')

# Aggregate CHIRPS data to monthly totals
df_CHIRPS['month'] = df_CHIRPS['Date'].dt.month
df_CHIRPS['year'] = df_CHIRPS['Date'].dt.year
monthly_CHIRPS = df_CHIRPS.groupby(['year', 'month']).sum(numeric_only=True).reset_index()
monthly_CHIRPS['Date'] = pd.to_datetime(monthly_CHIRPS['year'].astype(str) + '-' + monthly_CHIRPS['month'].astype(str), format='%Y-%m')

# Define the start date
start_date = pd.to_datetime('1981-01-01')

# Filter datasets to only include data starting from 1981-01-01
df_ANA = df_ANA[df_ANA['Date'] >= start_date]
df_ERA5 = df_ERA5[df_ERA5['Date'] >= start_date]
monthly_CHIRPS = monthly_CHIRPS[monthly_CHIRPS['Date'] >= start_date]

# Melt DataFrames (only necessary columns)
melted_ANA = df_ANA.melt(id_vars=['year', 'month', 'Date'], value_vars=df_ANA.columns[3:], var_name='Station', value_name='ANA')
melted_ERA5 = df_ERA5.melt(id_vars=['year', 'month', 'Date'], value_vars=code_columns, var_name='Station', value_name='ERA5_Land')
melted_CHIRPS = monthly_CHIRPS.melt(id_vars=['year', 'month', 'Date'], value_vars=monthly_CHIRPS.columns[3:], var_name='Station', value_name='CHIRPS_precip')

# Check unique values in Station columns
print("Unique Stations in melted_ANA:", melted_ANA['Station'].unique())
print("Unique Stations in melted_ERA5:", melted_ERA5['Station'].unique())
print("Unique Stations in melted_CHIRPS:", melted_CHIRPS['Station'].unique())

# Convert station identifiers in melted_ANA to match melted_ERA5 (remove leading zeros)
melted_ANA['Station'] = melted_ANA['Station'].str.lstrip('0')

# Ensure that melted DataFrames only include relevant columns for merging
melted_ANA = melted_ANA[['Date', 'Station', 'ANA']]
melted_ERA5 = melted_ERA5[['Date', 'Station', 'ERA5_Land']]
melted_CHIRPS = melted_CHIRPS[['Date', 'Station', 'CHIRPS_precip']]

# Merge melted DataFrames on both Station and Date
merged_df = pd.merge(melted_ANA, melted_ERA5, on=['Date', 'Station'], how='inner')
print('Merged DataFrame shape after ANA and ERA5:', merged_df.shape)

combined_df = pd.merge(merged_df, melted_CHIRPS, on=['Date', 'Station'], how='inner')
print('Combined DataFrame shape:', combined_df.shape)
print(combined_df.head())

# Prepare data for plotting
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
combined_df['Month'] = combined_df['Date'].dt.month_name()

# Create boxplot for all three datasets
plt.figure(figsize=(12, 6))
sns.boxplot(data=combined_df.melt(id_vars='Month', value_vars=['ANA', 'ERA5_Land', 'CHIRPS_precip'],
                                   var_name='Source', value_name='Precipitation'),
             x='Month', y='Precipitation', hue='Source', order=month_order)
plt.title('Comparison of Monthly Precipitation: ANA vs. ERA5 vs. CHIRPS')
plt.xlabel('Month')
plt.ylabel('Precipitation (mm)')
plt.xticks(rotation=45)
plt.legend(title='Data Source')
plt.tight_layout()
plt.show()

# After merging the DataFrames (assuming combined_df is already created)
# Calculate the bias
combined_df['Bias_ERA5'] = combined_df['ERA5_Land'] - combined_df['ANA']
combined_df['Bias_CHIRPS'] = combined_df['CHIRPS_precip'] - combined_df['ANA']

# Print the combined DataFrame with bias values
print(combined_df[['Date', 'Station', 'ANA', 'ERA5_Land', 'CHIRPS_precip', 'Bias_ERA5', 'Bias_CHIRPS']].head())

# Optionally, you can create boxplots for the bias values
plt.figure(figsize=(12, 6))
sns.boxplot(data=combined_df.melt(id_vars='Month', value_vars=['Bias_ERA5', 'Bias_CHIRPS'],
                                   var_name='Source', value_name='Bias Value'),
             x='Month', y='Bias Value', hue='Source', order=month_order)
plt.title('Monthly Bias: ERA5 vs. ANA and CHIRPS vs. ANA')
plt.xlabel('Month')
plt.ylabel('Bias (mm)')
plt.axhline(y=0, color='red', linestyle='--')  # Add a line at y=0 for reference
plt.xticks(rotation=45)
plt.legend(title='Data Source')
plt.tight_layout()
plt.show()