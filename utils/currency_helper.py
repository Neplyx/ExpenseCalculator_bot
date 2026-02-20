import requests
import time

cached_rates = None
last_update_time = 0

def get_currency_rates():
    global cached_rates, last_update_time
    if cached_rates and (time.time() - last_update_time < 600):
        return cached_rates

    try:
        # Додано timeout для стабільності
        response = requests.get("https://api.monobank.ua/bank/currency", timeout=10)
        if response.status_code == 200:
            data = response.json()
            rates = {"USD": None, "EUR": None}
            for item in data:
                # 840 - USD, 978 - EUR, 980 - UAH
                if item["currencyCodeB"] == 980:
                    buy = item.get("rateBuy") or item.get("rateCross")
                    sell = item.get("rateSell") or item.get("rateCross")
                    
                    if item["currencyCodeA"] == 840:
                        rates["USD"] = (float(buy), float(sell))
                    elif item["currencyCodeA"] == 978:
                        rates["EUR"] = (float(buy), float(sell))
            
            if rates["USD"] or rates["EUR"]:
                cached_rates, last_update_time = rates, time.time()
                return rates
    except Exception as e:
        print(f"Помилка валют: {e}")
    return cached_rates