numbers = [1, 2, 3]
v = numbers.copy()
new = []
for x in v:
    new.append(x)
    numbers.remove(x)

print(new)
print(numbers)