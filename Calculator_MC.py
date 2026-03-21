import datetime as dt
from collections import namedtuple

Currency = namedtuple("Cirrency", 'rate name')

class Record():
    def __init__(self, amount, comment, date=""):
        self.amount = amount
        self.comment = comment  
        if date == "": 
            self.date = dt.datetime.now().date()
        else: 
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()
        print(f"Расход: {self.amount} Комментарий: {self.comment} Дата: {self.date}")
        
class Calculator():
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, record):
        return self.records.append(record)
    def get_today_stats(self):
        today_rate = 0
        for s in self.records:
            if s.date == dt.datetime.now().date():
                today_rate += s.amount
        return(today_rate)
    def get_week_stats(self):
        week_rate = 0
        today = dt.date.today()
        week_ago = today - dt.timedelta(days= 7)
        for s in self.records:
            if week_ago <= s.date <= today:
                week_rate += s.amount
        return week_rate
    def today_stats(self):
        return (self.limit - self.get_today_stats())
    

class CashCalculator(Calculator):
    RUB_RATE = 1
    USD_RATE = 82.8
    EUR_RATE = 97.5

    CURRENCIES = {
        "rub": Currency(RUB_RATE, "Руб"),
        "usd": Currency(USD_RATE, "USD"),
        "eur": Currency(EUR_RATE, "EUR")
    }
    
    def conversion_rate(self, currencie: str):
        return self.CURRENCIES[currencie].rate
        
    def get_today_cash_remained(self, currencie):
        today_rate = self.today_stats()
        rate = today_rate / self.conversion_rate(currencie)
        currencie_name = self.CURRENCIES[currencie].name

        if rate == 0: 
            print("Денег нет, но вы держитесь")
        elif rate > 0: 
            print(f"Деньги осталось {rate} {currencie_name}")
        else: 
            print(f"Денег нет и ты в долгу на {rate} {currencie_name}")

    # class CaloriesCalculator(Calculator):
    #     def get_today_calories_remained():
    #         return

cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="кофе")) 
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))

print(cash_calculator.get_today_cash_remained("rub"))