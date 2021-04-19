import pandas as pd

url = "https://raw.githubusercontent.com/IshaanChawla0001/DataMining-final-project/main/bank-additional-full.csv"

data = pd.read_csv(url,sep=';')

print(data)

data.head()

data.to_csv('final_bank_dataset.csv')
