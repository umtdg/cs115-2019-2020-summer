class Element:
    def __init__(self, e_name, element_data):
        for key in element_data:
            try:
                element_data[key] = float(element_data[key])
            except:
                pass
        self.__eName = e_name.strip()
        self.__elementData = element_data

    def get_element_name(self):
        return self.__eName

    def get_property(self, property_name):
        if property_name in self.__elementData:
            return self.__elementData[property_name]
        return None

    def __lt__(self, other):
        return self.__eName < other.__eName

    def __eq__(self, other):
        if isinstance(other, Element):
            return self.__eName == other.__eName
        return False

    def __repr__(self):
        current_row = '\n\n| {:20}:  {:10}\n'.format('Element Name:', self.__eName)
        for key in self.__elementData:
            if type(self.__elementData[key]) == str:
                current_row += '| {:20}:  {:<10} \n'.format(key, self.__elementData[key])
            elif type(self.__elementData[key]) == float:
                current_row += '| {:20}:  {:<10.2f} \n'.format(key, self.__elementData[key])
        return current_row
