hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

#Calculating the total prices
for price in prices:
  total_price += price

#Finding the average price
average_price = total_price / len(prices)
print("Average Haircut Price: ", average_price)

#Using list compression to create a new list with each item reduced by 5 dollars
new_prices = [price - 5 for price in prices]
print(new_prices)

#Calculating total revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: ", total_revenue)

#Getting the average revenue of the week
average_daily_revenue = total_revenue / 7
print("Daily Average is: ", average_daily_revenue)


#Creating a new list for all hairstyles priced under 30 dollars
cut_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(cut_under_30)
