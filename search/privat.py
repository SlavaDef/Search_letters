import requests



def get_exchange_rates() -> str:
    url = "https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=5"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        result = []
        for currency in data:
            if currency['ccy'] in ['USD', 'EUR']:  # тільки ці валюти
                result.append(
                    f"<br>{currency['ccy']} => {currency['base_ccy']}:<br> BUY = {currency['buy']}, SELL = {currency['sale']} \n")

        return "".join(result)  # HTML-перехід на новий рядок

    else:
        return f"Помилка запиту: {response.status_code}"