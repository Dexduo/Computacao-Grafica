from math import sin

"""for i in range(1, 601):
    print("sin({}) = {}".format(i, sin(i)))"""

for x in range(0, 50): # we get the number of columns, that is the same as our width
        #value = int(199+((sin(x/10)-(1/2))*199))
        value = int(199+(sin(x/10)*199))
        print(value)