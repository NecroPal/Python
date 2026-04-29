#Positional Arguments
# def profile(name, age):
#     print("name :",name)
#     print("age :",age)
#     print(name, age)
#
# profile(21, "Taher")

#Default Arguments
# def profile(name, age, alive="yes"):
#     print("name :", name)
#     print("age :", age)
#     print("alive :", alive)
#     print(name, age, alive)
#
# profile("Taher", 21)

#Keyword Arguments
# def profile(name, age):
#     print("name :",name)
#     print("age :",age)
#     print(name, age)
#
# profile(age=21, name="Taher")

#Multiple Arguments(*args)
# def add(*num):
#     sum = 0
#     for i in num:
#         sum+=i
#         print(sum)
#
# add(5,10,15)

#Multiple Keyword Arguments(**kwargs)
def profile(**data):
    for i in data:
        print(data[i])

profile(name="Taher", age=21, phone="7416591653")
