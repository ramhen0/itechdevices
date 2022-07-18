#var="I am Human"
try:
    var
except NameError:
    print("well, it WASN'T defined after all!")
else:
    print(var)
