def dotOut(comp1, comp2):
    for x in range(0,200):
        comp1.append(".")
        comp2.append(".")

f = open('input.txt', 'r')
comp1 = []
comp2 = []
nums = []
sets = []
subset = 0
determiner = 0

dotOut(comp1, comp2)
print(comp1)
print(comp2)
for line in f:
    sets = line.split(",")
    for y in sets:
        nums = y.split("-")
        for z in range(int(nums[0]), int(nums[1])+1):
            if determiner == 0:
                comp1[z-1] = z
            else:
                comp2[z-1] = z

        determiner += 1
    determiner = 0

    set(comp1).remove(".")
    set(comp2).remove(".")
    if set(comp1).issubset(set(comp2)) or set(comp2).issubset(set(comp1)):
        subset += 1

    comp1 = []
    comp2 = []
    dotOut(comp1, comp2)

print(subset)
