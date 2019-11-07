import csv


class ParseCryptoData:
    def __init__(self,data):
        self.data = data
  
    def read_crypto_data(self):
        with open(self.data, 'r') as f:
            parsed_data = [row for row in csv.reader(f.read().splitlines())]           
        return parsed_data

    def get_min(self, parsed_data, col):
        col_list =[x[col] for x in parsed_data[1:]]
        value = [float(x) for x in col_list]
        return value.index(min(value))

    def get_max(self, parsed_data, col):
        col_list =[x[col] for x in parsed_data[1:]]
        value = [float(x) for x in col_list]
        return value.index(max(value)) 

    def hi_low_pct(self, parsed_data, today, yesterday):
        today_list = [x[today] for x in parsed_data[1:]]
        yesterday_list =[x[yesterday] for x in parsed_data[1:]]
        values = [(float(x) - float(y)) / float(y) * 100 for x, y in zip(today_list , yesterday_list)]
        return values [:10]    
    
    def pct_change(self, parsed_data, today, yesterday):
        today_list = [x[today] for x in parsed_data[1:]]
        yesterday_list =[x[yesterday] for x in parsed_data[1:]]
        values = [(float(y) - float(x)) / float(x) * 100 for x, y in zip(today_list , yesterday_list)]
        return round(values [0],2)



   
    



    

    