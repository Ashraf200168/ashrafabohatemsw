#create a reverse for a string in list 
coffees=['ESPRESSO','LATTE','CAPPUCCINO']
def reverse(str):
    return str[::-1]
reverse_coffees=map(reverse,coffees)
for x in reverse_coffees:
    print(x)
    