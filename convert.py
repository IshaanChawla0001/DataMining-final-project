import pandas as pd

url = "https://github.com/IshaanChawla0001/DataMining-final-project/blob/main/final_bank_dataset.csv"

data = pd.read_csv(url,sep=';')

print(data)

data.head()

data.to_csv('final_bank_dataset.csv')