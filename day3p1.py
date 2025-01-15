with open("day3.txt", "r") as file:
    str_content = file.read()

res = 0
nums = set("1234567890")  # Include 0 for all digits

i = 0
while i < len(str_content):
    j = i
    while j < len(str_content) and str_content[j] != "m":
        j += 1
    if j < len(str_content) and str_content[j:j+4] == "mul(":
        aux = j
        j += 4
        num1, num2 = [], []

        while j < len(str_content) and str_content[j] in nums:
            num1.append(str_content[j])
            j += 1

        while j < len(str_content) and str_content[j] not in nums and str_content[j] != ")":
            j += 1

        while j < len(str_content) and str_content[j] in nums:
            num2.append(str_content[j])
            j += 1

        if j < len(str_content) and str_content[j] == ")" and num1 and num2:
            number1 = int(''.join(num1))
            number2 = int(''.join(num2))
            res += number1 * number2
            print(str_content[aux:j+1])
        else:
            print(f"Invalid format: 'mul({''.join(num1)},{''.join(num2)}'")

    i = j + 1

print(f"The result is: {res}")
