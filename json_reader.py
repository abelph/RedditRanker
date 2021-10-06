import json

comments = []
i = 0
for line in open("C:/Users/abelp/Documents/Classes/Networks/Data/RS_politics_2016/RS_politics_2016.json", 'r'):
    comments.append(json.loads(line))
    i += 1
    if i >= 10000:
        break

print(comments[100])