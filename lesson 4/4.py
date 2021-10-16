from utils import currency_rates
print("Курс доллара: ", currency_rates("usd"))
print("Курс евро: ", currency_rates("eur"))
while True:
    code = input("Введите код валюты или 'Stop' для остановки: ")
    if code == "Stop":
        break
    print(currency_rates(code))