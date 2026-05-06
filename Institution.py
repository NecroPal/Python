class Institution:
    __institutionid = 0
    __institutionname = ""
    __numofstudentsplaced = 0
    __numofstudentscleared = 0
    __location = ""
    __grade = ""

    def __init__(self,instid,instname,placed,cleared,location):
        self.__institutionid = instid
        self.__institutionname = instname
        self.__numofstudentsplaced = placed
        self.__numofstudentscleared = cleared
        self.__location = location

    def getinstid(self):
        return self.__institutionid
    def setinstid(self,instid):
        self.__institutionid = instid

    def getinstname(self):
        return self.__institutionname
    def setinstname(self,instname):
        self.__institutionname = instname

    def getplaced(self):
        return self.__numofstudentsplaced
    def setplaced(self,placed):
        self.__numofstudentsplaced = placed

    def getcleared(self):
        return self.__numofstudentscleared
    def setcleared(self,cleared):
        self.__numofstudentscleared = cleared

    def getlocation(self):
        return self.__location
    def setlocation(self,location):
        self.__location = location

    def getgrade(self):
        return self.__grade
    def setgrade(self,grade):
        self.__grade = grade

class Solution:
    @staticmethod
    def findnumclearancedbyloc(lst,location):
        sum = 0
        for inst in lst:
            if inst.getlocation() == location:
                sum += inst.getcleared()
        return sum

    @staticmethod
    def updateinstitutiongrade(lst,instname):

        for inst in lst:
            if inst.getinstname() == instname:
                rating = (inst.getplaced()*100/inst.getcleared())
                if rating >= 80:
                    inst.setgrade("A")
                else:
                    inst.setgrade("B")
                return inst
        return None

if __name__ == "__main__":
    lst = []
    for i in range(4):
        instid = int(input())
        instname = input()
        placed = int(input())
        cleared = int(input())
        location = input()

        s = Institution(instid,instname,placed,cleared,location)
        lst.append(s)
    location = input()
    instname = input()

    print("-------------------\nOutput\n------------------")
    sum = Solution.findnumclearancedbyloc(lst,location)
    inst = Solution.updateinstitutiongrade(lst,instname)

    if sum > 0:
        print(sum)
    else:
        print("There are no cleared students in this particular location")

    if inst != None:
        print(inst.getinstname(),"::",inst.getgrade())
    else:
        print("No institute is available with the specified name")

# 111
# Amrita
# 5000
# 10000
# Chennai
# 222
# Karunya
# 16000
# 20000
# Coimbatore
# 333
# Appletech
# 10000
# 12000
# Chennai
# 444
# Aruna
# 6000
# 10000
# Vellore
# Chennai
# Karunya