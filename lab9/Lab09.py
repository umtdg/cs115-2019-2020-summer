from ChemicalOrder import ChemicalOrder
from Element import Element

chem_order = ChemicalOrder("data.txt")

chem_order.selection_sort_by_field("Atomic Number")
print("Elements sorted by 'Atomic Number':")
print(chem_order)

element_name = input("Enter name of element to search: ")
elem = chem_order.search_element(element_name)
if elem:
    print(elem)
else:
    print(f"Cannot found {element_name}")

max_quantity = int(input("Enter a quantity: "))
print(chem_order.get_element_by_quantity(max_quantity, chem_order.get_element_count()))
