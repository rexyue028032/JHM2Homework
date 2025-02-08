answer = int(input("Input Addition table size smaller 10:"))
print("Addition Table")
print("---------------------------------------------------------------------------------------------------")
for i in range(1,answer + 1):
    for p in range(1,answer + 1):
        sum_result = i + p
        if answer <= 10:
            print(f"{i} + {p} = {sum_result} ",end="")
    print()
print("---------------------------------------------------------------------------------------------------")