with open('advent-of-code.txt','r') as f:
    lines = f.read()
    my_array = lines.split("\n")


calorie_count = []
sum_of_calories = 0

for num in my_array:
    if num != '':
        sum_of_calories += int(num)
    else:
        calorie_count.append(sum_of_calories)
        sum_of_calories = 0
print(max(calorie_count))
print(sum(list(reversed(sorted(calorie_count)))[0:3]))

    
    



    

