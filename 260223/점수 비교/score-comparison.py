math_a, eng_a = input().split()
math_b, eng_b = input().split()


if int(math_a) > int(math_b) and int(eng_a) > int(eng_b):
    print(1)
else:
    print(0)