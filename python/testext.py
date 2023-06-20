file = open("data.txt", "w")
content = file.write("this is my teacher, he is not bad.")
file.close()

file = open("data.txt", "r")
string = file.read()
binary_converted = ' '.join(format(ord(c), 'b') for c in string)
print("The Binary Representation is:", binary_converted)
file.close()

file = open("test-one.bin", "w")
content = file.write(binary_converted)
file.close()