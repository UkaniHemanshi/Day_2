import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class StockData:
    # date = []
    # close =[]
    def __init__(self,path):
        self.path = path

    def load_data(self):
        try:
            self.df = pd.read_csv(self.path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found. Please check the path.")
        except pd.errors.EmptyDataError:
            print("No data found in the file.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            return self.df

    def sort_data(self,df1):
        df = df1.sort_values(by='Date')
        return df

    def visualize(self,df1):

        # barchart
        df = df1.head()
        plt.figure(figsize=(12, 15))
        plt.bar(df["Date"],df["Close"], color='skyblue')
        plt.title('Bar Chart example')
        plt.xlabel('Date')
        plt.ylabel('Close')
        plt.show()



obj1 = StockData('apple_stockdata.csv')
df1 = obj1.load_data()
print(f"Datafrme of csv :{df1}")
print(obj1.sort_data(df1))
obj1.visualize(df1)
