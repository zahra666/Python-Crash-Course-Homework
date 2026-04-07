names = ['David','Susan','Kitty']
print(names)
names.remove('Susan')
print(names)
names.append('Herry')
print(names)

names.insert(0,'Zoctopus')
names.insert(2,'Lianlian')
names.append('Niannian')
print(names)

#pop进行删除
names_pop1 = names.pop()
print(f"Sorry, {names_pop1}, I cannot invite you.")
names_pop2 = names.pop()
print(f"Sorry, {names_pop2}, I cannot invite you.")
names_pop3 = names.pop()
print(f"Sorry, {names_pop3}, I cannot invite you.")
names_pop4 = names.pop()
print(f"Sorry, {names_pop4}, I cannot invite you.")

print(f"names[0], you are still invited.")
print(f"names[1], you are still invited.")

del names[1]
print(names)
del names[0]
print(names)
