import json
import requests

with open("lang.json") as json_file:
    lang_file = json.load(json_file)

for i, (key, value) in enumerate(lang_file.items(), 1):
    print(f"{key}. {value['lang']}")

while True:
    lang = str(input("Language: "))

    if lang_file.get(lang) is None:
        print("This language does not exist")
    else:
        break

while True:
    print(f"1. {lang_file[lang]['text']['option1_input']}")
    print(f"2. {lang_file[lang]['text']['option2_input']}")
    option = int(input(f"{lang_file[lang]['text']['selection_option']}: "))

    response = requests.get("https://s3.amazonaws.com/dolartoday/data.json")
    data = json.loads(response.text)

    dollar_price_in_bolivars = float(data["USD"]["dolartoday"])

    if option == 1:
        dollar_amount = float(input(f"{lang_file[lang]['text']['if_option1_input']}: "))
        bolivar_amount = dollar_amount * dollar_price_in_bolivars
        print(f"{dollar_amount} {lang_file[lang]['text']['dollars']} {lang_file[lang]['text']['equals']} {bolivar_amount} {lang_file[lang]['text']['bolivars']}")
        break
    elif option == 2:
        bolivar_amount = float(input(f"{lang_file[lang]['text']['if_option2_input']}: "))
        dollar_amount = bolivar_amount / dollar_price_in_bolivars
        print(f"{dollar_amount} {lang_file[lang]['text']['bolivars']} {lang_file[lang]['text']['equals']} {bolivar_amount} {lang_file[lang]['text']['dollars']}")
        break
    else:
        print(f"{lang_file[lang]['text']['invalid_option']}")

    