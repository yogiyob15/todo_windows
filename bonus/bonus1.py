feet_inches = input("Enter your height in feet and inches :")

def parse(feetinches):
    part = feetinches.split(" ")
    feet = float(part[0])
    inch = float(part[1])
    return feet, inch


def convert(feet_arg, inch_arg):
    return feet_arg * 0.3040 + inch_arg * 0.02454


f, i = parse(feet_inches)
print(f, i)
result = convert(f, i)

if result > 1:
    print("Kids can use the slides")
else:
    print("Kids cannot use slides")


