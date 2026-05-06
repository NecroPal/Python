class Solution:
    def add(self,a,b):
        return a+b

    def add(self,a,b,c):  #method overloading
        return a+b+c

s = Solution()
print(s.add(1,2,4))
print(s.add(1,2,3))