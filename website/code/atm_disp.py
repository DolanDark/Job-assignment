def currency_sort(val):
    den = [100, 20, 10, 5, 1]
    val = int(val)

    #val = int(input("Enter the amount: "))
    temp = val
    scoop = []

    for i in range(0,len(den)):
        temp2 = int(temp/den[i])
        if (temp2):
            scoop.append(f'{temp2} units of the denomination {den[i]}')

        temp = temp%den[i]

    full_str = " | ".join([str(i) for i in scoop])
    return full_str

# a1 = currency_sort("535")
# print(a1)