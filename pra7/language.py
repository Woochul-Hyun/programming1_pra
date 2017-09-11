from pra7.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(ruby)
print(python)
print(vb)

list = [ruby, python, vb]
list_dynamic = []
for each in list:
    dynamic = each.is_dynamic()
    if dynamic == True:
        list_dynamic.append(each.name)
print("Dynamically typed languages are:")
for i in list_dynamic:
    print(i)