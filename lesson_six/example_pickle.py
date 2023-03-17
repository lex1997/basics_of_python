import pickle

filename = 'example.pickle'

data = {
    "Имя": "Алексей",
    "Фамилия": "Гневашев",
    "Отчество": "Дмитриевич",
    "Возраст": "26",
    "Пол": "мужской",
}

with open(filename, "wb") as file:
    pickle.dump(data, file)

with open(filename, "rb") as file:
    print(pickle.load(file))
