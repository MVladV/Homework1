import re

variables = {}
formula = input('Insert formula: ')
while True:
    try:
        res = eval(formula, variables)
    except NameError as e:
        v = re.match('name .(\w+). is not defined', e.message).group(1)
        variables[v] = input('insert value for %s: ' % v)
        continue
    print ("True, %s" % (res))
    break
