import numpy as np
import Element

class ChemicalOrder:
    def __init__(self, filename):
        self.__e_list = []

        self.load_elements(filename)

    def load_elements(self, filename):
        data = np.loadtxt(filename, delimiter="\t", dtype=np.str)

        data = np.char.strip(data)

        property_names = data[0, :]
        data = data[1:, :]

        name_col_index = np.where(property_names == "Name")[0][0]

        self.__e_list = []
        for i in range(len(data)):
            row = data[i]

            name = row[name_col_index]
            properties = {}

            for j in range(0, len(row)):
                if j != name_col_index:
                    properties[property_names[j]] = row[j]

            self.__e_list.append(Element.Element(name, properties))

    def get_element_count(self):
        return len(self.__e_list)

    def sort_elements(self):
        self.__e_list.sort()

    def selection_sort_by_field(self, property_name):
        # a sorted array to get minimum value easily
        property_values = []

        # a dictionary for index lookup in format value: index
        indexes = {}

        for i in range(len(self.__e_list)):
            property_value = self.__e_list[i].get_property(property_name)
            property_values.append(property_value)
            indexes[property_value] = i

        property_values.sort()

        for i in range(len(self.__e_list) - 1):
            # const time for dictionary lookup
            min_index = indexes[property_values[i]]

            # swap the elements
            self.__e_list[i], self.__e_list[min_index] = self.__e_list[min_index], self.__e_list[i]

            # also swap the indexes in the dictionary
            indexes[self.__e_list[i].get_property(property_name)] = i
            indexes[self.__e_list[min_index].get_property(property_name)] = min_index

    def search_element(self, element_name):
        max_index = len(self.__e_list) - 1
        min_index = 0

        self.sort_elements()

        while min_index <= max_index:
            mid_index = (max_index + min_index) // 2
            mid = self.__e_list[mid_index].get_element_name()

            if element_name > mid:
                min_index = mid_index + 1
            elif element_name < mid:
                max_index = mid_index - 1
            else:
                return self.__e_list[mid_index]

        return None

    def get_element_by_quantity(self, max_quantity, count):
        if count > 0:
            if self.__e_list[count - 1].get_property("Quantity") < max_quantity:
                if count == 1:
                    return [self.__e_list[count - 1]]
                else:
                    return self.get_element_by_quantity(max_quantity, count - 1) + [self.__e_list[count - 1]]
            else:
                return self.get_element_by_quantity(max_quantity, count - 1)
        else:
            return []

    def __repr__(self):
        result = ""
        for elem in self.__e_list:
            result += repr(elem)

        return result
