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
    
    set1 = set(comp1)
    set2 = set(comp2)

    set1.remove(".")
    set2.remove(".")
    print(set1)
    print(set2)
    
    if not set1.isdisjoint(set2) or not set2.isdisjoint(set1):
        subset += 1
    print("Subset: ", subset)

    comp1 = []
    comp2 = []
    dotOut(comp1, comp2)

print(subset)
