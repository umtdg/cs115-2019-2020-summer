import employee


class PartTime(employee.Employee):
    def __init__(self, name, idnum, wage, hours):
        super(PartTime, self).__init__(name, idnum, wage)

        self.__hours = hours

    # hours
    def get_hours(self):
        return self.__hours

    def __repr__(self):
        return "Name: {0} Employee ID: {1} Wage: {2} Hours: {3}".format(
            self.get_empName(),
            self.get_idNum(),
            self.get_wage(),
            self.__hours
        )

    def calculate_salary(self):
        total_wage = self.get_wage() * self.__hours
        return total_wage - (total_wage * self.get_taxRate())
