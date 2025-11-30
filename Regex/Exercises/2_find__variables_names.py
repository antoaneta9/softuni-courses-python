import re
text = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
result = re.findall(pattern, text)
# print(result)
res=[]
for item in result:
    res.append(item.replace('_', ''))
print(','.join(res))