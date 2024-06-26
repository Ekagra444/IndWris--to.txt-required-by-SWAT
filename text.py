import pandas as pd

# Load the CSV file
csv_file_path = r'E:\\downloads\\mahanadi imd.csv'
data = pd.read_csv(csv_file_path)

# Assuming your CSV has columns named 'Date' and 'Rainfall'
# And the Date is in 'MM-YY' format
data['Date'] = pd.to_datetime(data['Date'], format=r'%b-%y')

# Extract year, month
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month


# Arrange columns in the order required by SWAT ('Rainfall')
swat_data = data[['Rainfall']]

# Save to .txt file
txt_file_path = r'E:\\downloads\\mahanadiF.txt'
swat_data.to_csv(txt_file_path, sep=' ', index=False, header=False)
