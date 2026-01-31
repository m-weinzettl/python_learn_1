import test
import markus
import steffi

print("tst")

liste = [1, 2, 3, 4, 5]

liste = (x * 2 for x in liste)

dictionary = {x: x * 2 for x in range(5)}

print(test.show_test())

#hier steht mein code zum testen von markus.py
print(markus.print_name())
markus.test_print()
markus.test_count()
print(markus.test_merge())
print(markus.test_list_comp())
print(markus.test_name_merge())

#test steffi.py (hab code von markus integriert)
steffi.demo_lists_noob()