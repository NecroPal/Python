class Bank: #Name of class should always be capital
    accno = 0
    name = ""

    def __init__(self, accno, name): #self - current instance of class
        self.accno = accno
        self.name = name

    def show(self):
        print("AccNo:",self.accno)
        print("Name:",self.name)

b = Bank(599800, "Taher Nawab")
b2 = Bank(500800, "Hiten")
print(b.name)
b.show()
b2.show()