#Creating Bussiness class
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises



#Defining Francise class
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
# Creating a available_menu method to tell customers available orders
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

#Giving a string representation method to Franchise Class
  def __repr__(self):
    return self.address

# Defining class menu
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
#Giving a string representation method to Menu Class
  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + 'hrs' + ' - ' + str(self.end_time) + 'hrs'

    #Defining
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

#Declaring brunch menu items
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

#Instantiating brunch menu
brunch = Menu("brunch", brunch_items, 1100, 1600)

#Using calculate_bill function to get total bill for customers on brunch
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

#Declaring early_bird menu items
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

#Instantiating brunch menu
early_bird = Menu("early_bird", early_bird_items, 1500, 1800)

#Using calculate_bill function to get total bill for customers on early_bird menu
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

#Declaring dinner menu items
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
#Instantiating dinner menu
dinner = Menu("dinner", dinner_items, 1700, 2300)

#Declaring kids menu items
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}


#Instantiating kids menu
kids = Menu("kids", kids_items, 1100, 2100)
print(kids)

#Creating an array of all menus
menus = [brunch, early_bird, dinner, kids]


#Creating instances of franchises and passing it an array of all menus
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

#Instantiating Business class
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])


# Arepos
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
#Creating arepas menu
arepas_menu = Menu("Take a’ Arepa", arepas_items, 1000, 2000)


#Creating arebas franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#Creating arepa business
arepa = Business("Take a' Arepa", [arepas_place])

print(arepa.franchises[0].menus[0])


