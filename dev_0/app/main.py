import test
import markus

print("tst")

liste = [1, 2, 3, 4, 5]

liste = (x * 2 for x in liste)

dictionary = {x: x * 2 for x in range(5)}

print(test.show_test())

#hier steht mein code zum testen von markus.py
print(markus.print_name())
