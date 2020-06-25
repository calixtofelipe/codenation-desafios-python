
class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    # Proteja a classe `Employee` para não ser instânciada diretamente
    def __new__(cls, *args, **kwargs):
        if cls == Employee:
            raise TypeError(
                "Essa classe não pode ser instanciada diretamente.")
        return super(Employee, cls).__new__(cls)

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    # Torne obrigatório a implementação dos métodos da classe `Employee`
    def calc_bonus(self):
        raise NotImplementedError("Obrigatorio implementar")

    # Torne obrigatório a implementação dos métodos da classe `Employee`
    def get_hours(self):
        raise NotImplementedError("Obrigatorio implementar")
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)
        # Proteja o atributo `department` da classe `Manager` para que seja
        # acessado somente através do método `get_department`

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return 8
    # Proteja o atributo `department` da classe `Manager` para que seja
    # acessado somente através do método `get_department`

    def get_departament(self):
        return self.__departament.name

    def set_department(self, name):
        self.__departament.name = name


class Seller(Employee):
    # Seller tem que herdar de Employee
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        # Proteja o atributo `department` da classe `Manager` para que seja
        # acessado somente através do método `get_department`
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_hours(self):
        return 8

    def get_departament(self):
        return self.__departament.name

    def get_sales(self):
        return self.__sales

    def put_sales(self, new_value):
        self.__sales += new_value

    def set_department(self, name):
        self.__departament.name = name

    def calc_bonus(self):
        return self.__sales * 0.15
