# Напишите программу для печати всех уникальных значений в словаре.
dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

col = []
for i in dict:
    print(i.values())
    col = col + list(i.values())

print(col)
print(list(set(col)))