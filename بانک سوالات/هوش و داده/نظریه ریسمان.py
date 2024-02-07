findStr = input()
sentense = input()
print(*[1 if sentense.find(findStr) != -1 else 0])