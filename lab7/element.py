def __try_float__(text):
    if not text:
        return False

    if text.startswith("-"):
        text = text[1:]

    text = text.split(".")
    if len(text) != 2:
        return False

    p = bool(text[0])
    q = bool(text[1])
    r = text[0].isdigit()
    s = text[1].isdigit()

    if p and q:
        return r and s
    elif p and not q:
        return r and not s
    elif not p and q:
        return not r and s
    else:
        return r and s


class Element:
    def __init__(self, name, properties):
        # Convert to float if possible
        # (better to check with try/except or regex)
        for prop_name in properties.keys():
            if __try_float__(properties[prop_name]):
                properties[prop_name] = float(properties[prop_name])

        self.__eName = name
        self.__elementData = properties

    def __eq__(self, other):
        return other.__eName == self.__eName

    def __lt__(self, other):
        return self.__elementData["Atomic Number"] < \
               other.__elementData["Atomic Number"]

    def __repr__(self):
        return(f"""
        | Element Name      : {self.__eName}
        | Chemical Symbol   : {self.__elementData["Chemical symbol"]}
        | Origin of Symbol  : {self.__elementData["Origin of symbol"]}
        | Atomic Number     : {self.__elementData["Atomic Number"]}
        | Atomic Mass       : {self.__elementData["Atomic mass"]}
        | Density           : {self.__elementData["Density"]}
        | Melting Point     : {self.__elementData["Melting point"]}
        | Boiling Point     : {self.__elementData["Boiling point"]}
        | Year of Discovery : {self.__elementData["Year of discovery"]}
        | Discoverer        : {self.__elementData["Discoverer"]}
        """)

    def get_property(self, prop_name):
        if prop_name in self.__elementData.keys():
            return self.__elementData[prop_name]
        else:
            return None
