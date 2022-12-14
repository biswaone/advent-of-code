priority = {chr(i+96):i for i in range(1,27)}
capital_priority = {chr(i+65):i+27 for i in range(0,26)}
priority.update(capital_priority)

priority_sum = 0
priority_sum_2 = 0

with open('advent-of-code-3.txt','r') as f:
    rucksacks = f.read().split("\n")
    for rucksack in rucksacks:
        if rucksack != '':
            str1 = rucksack[0:len(rucksack)//2]
            str2 = rucksack[len(rucksack)//2 :len(rucksack)]
            intersect = list(set(str1).intersection(str2))[0]
            priority_sum += priority[intersect]

    start = 0
    end = 3

    while (start<=end and end<= len(rucksacks)):
        s1 = rucksacks[start:end][0]
        s2 = rucksacks[start:end][1]
        s3 = rucksacks[start:end][2]

        common = list(set(s1).intersection(s2).intersection(s3))[0]
        priority_sum_2 += priority[common]

        start += 3
        end += 3

print(priority_sum)
print(priority_sum_2)




            
