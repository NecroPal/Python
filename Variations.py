#No return no argument
def greet():
    print("Sab Badiya")

#No return with argument
def greeting(name):
    print(name, "Sab Khairiyat?", sep="@")

#Return with no argument
def greets():
    return "Great"

#Return with argument
def greetings(name):
    return "waah "+name

# greeting("Taher")
name = greetings("Taher")
print(name)