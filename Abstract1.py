class Meal:
    def __cookRajma(self):
        print("Rajma Prepared")
    def __cookRumaliRoti(self):
        print("Rumali Roti Prepared")
    def __preparesalad(self):
        print("Salad Prepared")
    def __cookrice(self):
        print("Rice Prepared..")
    def __Sweet(self):
        print("Sweet Prepared..")

    def cookmeal(self):
        self.__cookRajma()
        self.__cookRumaliRoti()
        self.__preparesalad()
        self.__cookrice()
        self.__Sweet()

if __name__ == "__main__":
    m = Meal()
    m.cookmeal()