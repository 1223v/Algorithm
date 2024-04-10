num = input("입력: ")
tmp = num.replace("$","")
result = int(tmp.replace(",",""))*2
print(result)