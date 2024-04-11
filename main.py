# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
# calculateMonetary profit total
profit = (retailPrice) - (wholesalePrice)
# calculateMonetary salePrice total
salePrice = (retailPrice) * (0.75)
# calculateMonetary saleProfit total
saleProfit = (salePrice) - (wholesalePrice)

# Write your assignment statements here for profit, salePrice, and saleProfit

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
# displayText profit total
print("Profit: $" + str(profit))
# displayText salePrice total
print("Sale Price: $" + str(salePrice))
# displayText saleProfit total
print("Sale Profit: $" + str(saleProfit))
