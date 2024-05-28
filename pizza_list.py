#Lists of Kind of Pizzas i sell
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#List of costs of pizza slice
prices = [2, 6, 1, 3, 2, 7, 2]

#Finding occurrences of $2 dollar slices
num_two_dollar_slices = prices.count(2)

#finding the lenght of toppings list and assigning variable to it
num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kind of pizza!")

#Combining two lists to have a two-dimensional list
pizza_and_prices = [
[2, "pepperoni"],
[6, "pineapple"],
[1,	"cheese"],
[3,	"sausage"],
[2,	"olives"],
[7,	"anchovies"],
[2,	"mushrooms"],
]

print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)

#Getting the cheapest and the expensive pizza
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

#Removing the last expensive pizza
pizza_and_prices.pop()

#Adding another pizza
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

#Slicing the 3 lowest cost pizzas from the list
three_cheapest = pizza_and_prices[:3]
print(pizza_and_prices)

print(three_cheapest)


