s = input("Enter string: ")

max_char = ""
max_count = 0

for i in s:
    if i.isalpha():
        c = 0
        for j in s:
            if i == j:
                c += 1
        if c > max_count:
            max_count = c
            max_char = i

print(max_char, max_count)
