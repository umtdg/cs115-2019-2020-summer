class Employee:
    __taxRate = .40

    def __init__(self, name, idnum, wage):
        self.__empName = "default"
        self.__idNum = 99999
        self.__wage = 0

        self.set_empName(name)
        self.set_idNum(idnum)
        self.set_wage(wage)

    # empName
    def get_empName(self):
        return self.__empName

    def set_empName(self, value):
        for c in value:
            if not c == " " or c.isalpha():
                self.__empName = "default"

        self.__empName = value

    # idNum
    def get_idNum(self):
        return self.__idNum

    def set_idNum(self, value):
        try:
            self.__idNum = int(value)
        except:
            self.__idNum = 99999

    # wage
    def get_wage(self):
        return self.__wage

    def set_wage(self, value):
        if value >= 0:
            self.__wage = value
        else:
            self.__wage = 0

    # taxRate
    def get_taxRate(self):
        return Employee.__taxRate

    def __lt__(self, other):
        self_name = self.__empName.split(" ")
        other_name = other.__empName.split(" ")

        if self_name[1] == other_name[1]:
            return self_name[0] < other_name[0]

        return self_name[1] < other_name[1]

    def __eq__(self, other):
        return self.__idNum == other.__idNum

    def __repr__(self):
        return "Name: {0} Employee ID: {1} Wage: {2}".format(
            self.__empName,
            self.__idNum,
            self.__wage
        )

    def calculate_salary(self):
        return self.__wage - (self.__wage * Employee.__taxRate)
