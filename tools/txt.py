f = open("test.json","r")
contents = f.readlines()
f.close()

contents.insert(0,"{\n")
contents.insert(1,'"traceObj" :')

f = open("test.json","w")
contents = "".join(contents)
f.write(contents)
f.close()

count = 0

with open("test.json","r") as f:
	for i in f:
		count += 1

f = open("test.json","r")
contents = f.readlines()
f.close()

count += 2

contents.insert(3,"\n}")

f = open("test.json","w")
contents = "".join(contents)
f.write(contents)
f.close()