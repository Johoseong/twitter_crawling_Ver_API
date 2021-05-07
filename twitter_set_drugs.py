import pandas as pd


class Drugs:
    lists = []

    def __init__(self):
        df = pd.read_csv("drug_brand.csv")
        data = df.columns
        data = data.tolist()
        for drugname in data:
            brand = self.setFromCsv(df, drugname)
            self.lists.append(brand)

    def setFromCsv(self, df, drugname):
        data = df[drugname]
        data = data.values
        data = data.tolist()
        data = [x for x in data if pd.isnull(x) == False]
        return data
