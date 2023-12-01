data = open("input.txt", "r")
total = 0
for line in data:
    # replaces the word with the number for each group
    group_one = line.replace("one", '1').replace("nine", '9').replace("five", '5').replace("\n", '')
    group_two = line.replace("two", '2').replace("three", "3").replace("four", '4').replace("\n", '')
    group_three = line.replace("six", "6").replace("seven", '7').replace("eight", '8').replace("\n", '')

    index = 0
    # breaks at the first non-alpha character amongst the three strings
    while group_one[index].isalpha() and group_two[index].isalpha() and group_three[index].isalpha():
        index = index + 1
    # sets tens equal to the number
    if not group_one[index].isalpha():
        tens = int(group_one[index])
    elif not group_two[index].isalpha():
        tens = int(group_two[index])
    else:
        tens = int(group_three[index])

    index = -1
    # breaks at the last number in each of the 3 strings
    while group_one[index].isalpha() and group_two[index].isalpha() and group_three[index].isalpha():
        index = index - 1
    if not group_one[index].isalpha():
        ones = int(group_one[index])
    elif not group_two[index].isalpha():
        ones = int(group_two[index])
    else:
        ones = int(group_three[index])
    # adds the number to the total
    total = total + (tens * 10) + ones
print("total = ", total)
