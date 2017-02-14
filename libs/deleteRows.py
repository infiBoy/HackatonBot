with open("senteces.json") as f:
    lines = [x for x in f]

with open("clearSenteces.json", 'w') as newf:
    newf.writelines(list(set(lines)))
