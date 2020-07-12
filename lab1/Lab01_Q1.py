# a:
battery_mass = float(input("Enter battery mass: "))
cable_mass = float(input("Enter battery cable mass: "))
print("Total mass: ", battery_mass + cable_mass)

# b:
print("Total mass with one cable removed: ", battery_mass + cable_mass/2)

# c:
print("Mass of two batteries: ", battery_mass * 2)

# d:
print("Density of battery with m=5000g, V=2500 cubic cm: ", 5000/2500)

# e:
print("Area of the battery with edges 3cm: ", 3**2)

# f:
print("Volume of the battery with edges 3cm: ", 3**3)
