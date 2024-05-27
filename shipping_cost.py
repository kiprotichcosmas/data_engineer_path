weight = 41.5


if weight <= 2:
  cost_ground = weight * 1.5 + 20

elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20

elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20

elif weight > 10:
  cost_ground = weight * 4.75 + 20

cost_ground_premium = 125.00

print("The Ground Shipping Premium $", cost_ground_premium)
print("The Ground Shipping Cost for your goods is of " + str(weight) + "pounds is " + str(cost_ground))


#Drone Shipping
if weight <= 2:
  cost_drone_shipping = weight * 4.5

elif weight > 2 and weight <= 6:
  cost_drone_shipping = weight * 9

elif weight > 6 and weight <= 10:
  cost_drone_shipping = weight * 12

elif weight > 10:
  cost_drone_shipping = weight * 14.25
  
print("The Drone Shipping Cost for your goods is " + str(weight) + "pounds is " + str(cost_drone_shipping))
