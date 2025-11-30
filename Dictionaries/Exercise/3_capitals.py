
countries = input().split(', ')
capitals = input().split(', ')
pairs = {key: value for key, value in zip(countries, capitals)}
# print(pairs)
for key, value in pairs.items():
    print(f"{key} -> {value}")