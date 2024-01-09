Облаштувати Переведення валют в обмінику через словник(приклад структури на гітхабі)
Загорнути код що робить конвертацію та розраховує курс продажу в фунції.
В словнику дані кількість купюр кожного номіналу. Зробити фунцію яка перевіряє чи вистачить коштів чи купюр щоб обміняти гроші..








AUH_EUR_BUY = 42.00
AUH_USD_BUY = 40.00
AUH_PLN_BUY = 30.00
AUH_EUR_CELL = AUH_EUR_BUY + (AUH_EUR_BUY * 0.05)
AUH_USD_CELL = AUH_USD_BUY + (AUH_USD_BUY * 0.05)
AUH_PLN_CEll = AUH_PLN_BUY + (AUH_PLN_BUY * 0.05)
PROFIT_PRC = 5#5%

current ={
    "UAH": {
        "buy":{
            "USD":40,
            "EUR":36,
            "PLN":6,
        },
        "sell": {}
    }
}
currency = {100:2, 50:10, 20:0, 10:0, 5:100, 2:10, 1:10}

print(f"{'':*^15}")
print(f"{'*BUY':<5}{'':5}{'SELL*':>5}")
print(f"*{AUH_EUR_BUY:<5}{'EUR':^3}{AUH_EUR_CELL:>5}*")#loop
print(f"*{AUH_USD_BUY:<5}{'USD':^3}{AUH_USD_CELL:>5}*")#loop
print(f"*{AUH_PLN_BUY:<5}{'PLN':^3}{AUH_PLN_CEll:>5}*")#loop
print(f"{'':*^15}")

val_uah = float(input("Введіть кількість гривень, яку ви хочете продати: "))
result = val_uah // AUH_USD_BUY
remain = val_uah % AUH_USD_BUY

print(f"Ваша валютa {result} дол")
print(f"Ваша решта {remain:>7} грн")
