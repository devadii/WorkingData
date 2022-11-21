# import requests
# from bs4 import BeautifulSoup
import json

# url = "https://educatebox.com/114-list-of-qurani-surah-with-para-quran-all-surah-names"
# data = requests.get(url).text

# soup = BeautifulSoup(data, "html.parser")

# required_table = soup.find('table').find("tbody")
# del required_table[0]
# info = {}

# x = 1

# for index, row in enumerate(required_table):
#     if index != 0:
#         coloumn = row.find_all('td');
#         info[f"{x}"] = {
#             "text": coloumn[2].text.strip(),
#             "verse": coloumn[3].text.strip()
#         }
#         x = x + 1

# final_data = str(info)

# with open("info.json", 'w', encoding="utf-8") as info:
#     info.write(final_data)


main_arr = []

with open('eng.json', 'r', encoding="utf-8") as infoFile:
    info = json.load(infoFile)

for surah in info:

    sub_data = {
        "id": surah["id"],
        "name": surah["name"],
        "total_verses": surah["total_verses"],
        "verses": []
    }

    for ayat in surah["verses"]:

        single_ayat = {
            "id": ayat["id"],
            "text": ayat["text"],
            "translation": {
                "en_ur": "",
                "en_en": ayat["translation"].replace('"',"+++").replace("'", "+++")
            }
        }

        sub_data["verses"].append(single_ayat)

    main_arr.append(sub_data)

final_data = str(main_arr)

with open("final_data.json", 'w', encoding="utf-8") as fData:
    fData.write(final_data)