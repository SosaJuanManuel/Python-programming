a = 4
b = 3.14
c = "Soy un simple String"
d = False
e = 5 + 3j

print(1,")",a + b,
	2,")",a * b,
	3,")",b * b,
	4,")",a ** a,
	5,")",a ** b,
	6,")",c + c,
	7,")",c * a,
	8,")",a / 3,
	9,")",a // 3,
	10,")",a % 3)

print("------------------")

print (1,")",type(a + b),
	2,")",type(a * b),
	3,")",type(b * b),
	4,")",type(a ** a),
	5,")",type(a ** b),
	6,")",type(c + c),
	7,")",type(c * a),
	8,")",type(a / 3),
	9,")",type(a // 3),
	10,")",type(a % 3))
	
print("------------------------")

print(not True,
	True and False,
	True or False,
	not True and not False)
print("----------------------")

print(1,")",bool(""),
	2,")",bool("Soy un string"),
	3,")",bool(0),
	4,")",bool(1),
	5,")",5 and True,
	6,")",7 and False, 
	7,")","" and True,
	8,")","soy un simple string" and True,
	9,")","A" and "B")