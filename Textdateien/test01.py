# test01.py

file = open("test01.txt", "r")

content = file.readlines()

file.close()

for index, zeile in enumerate(content):
    print(str(index) + ": " + zeile.strip())

out = open('test01_ausgabe.txt', 'a')
out.write(content[0]*5)
out.close()




