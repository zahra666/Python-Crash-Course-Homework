pizza_list = ['red pizze','yellow pizza','green pizza']
friend_pizzas = pizza_list[:]

pizza_list.append('blue pizza')
friend_pizzas.append('black pizza')

print(pizza_list)
print(friend_pizzas)

print("My favorite pizzas are:")
for myp in pizza_list:
    print(myp)
        
print("\n My friend's favorite pizzas are:")
for frp in friend_pizzas:
    print(frp)
