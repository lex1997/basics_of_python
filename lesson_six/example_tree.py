import json

data = {
    "Имя": "Алексей",
    "Фамилия": "Гневашев",
    "Отчество": "Дмитриевич",
    "Возраст": "26",
    "Пол": "мужской",
}

with open('example.json', 'w', encoding="utf-8") as file:
    file.write(json.dumps(data, ensure_ascii=False))

result = []
with open('example.json', encoding="utf-8") as file:
    print(type(file.read()))