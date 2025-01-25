price1 = int(input("Enter a price:"))
price2 = int(input("Enter a another price:"))
if price1 > price2:
    print("the first price is larger than the second one.")
elif price1 < price2:
    print("The first price is smaller than the second one.")
else:
    print("The price are the same.")