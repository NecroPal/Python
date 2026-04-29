#Call by Value - for immutable data types
# def update(v):
#     v = 10
#     print(v)
#
# v = 5
# update(v)
# print(v)

#Call by Reference - for mutable data types
def update(lst):
    lst[0]=21

lst = [10,20,30,40,50]
update(lst)
print(lst)