a = int(input("Zadejte první člen posloupnosti: "))
d = int(input("Zadejte rozdíl posloupnosti: "))
print("sečíst posloupnost")
for i in range(5):
    print(a)
    a = a + d
print("součet posloupnosti")
soucet = 0
for i in range(5):
    print(a)
    a = a + d
    soucet = soucet + a