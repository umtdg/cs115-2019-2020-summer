import numpy as np
import element

data = np.loadtxt("data.txt", delimiter="\t", dtype=np.str)

# remove unnecessary whitespaces from data
data = np.char.strip(data)

# get the first row and delete it
property_names = data[0, :]
data = data[1:, :]

# get index of name column
name_col_index = np.where(property_names == "Name")[0][0]

elements = []
for i in range(len(data)):
    row = data[i]

    name = row[name_col_index]
    properties = {}

    for j in range(0, len(row)):
        # skip name
        if j != name_col_index:
            properties[property_names[j]] = row[j]

    elements.append(element.Element(name, properties))

elements.sort()
for elem in elements:
    print(elem)

discoverer = input("Enter name of discoverer: ")
discovers = [elem for elem in elements if elem.get_property("Discoverer") == discoverer]

if discovers:
    print(f"{discoverer} discovered: ")
    for elem in discovers:
        print(elem)
else:
    print("No such discoverer")
