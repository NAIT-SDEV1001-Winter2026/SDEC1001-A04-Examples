# 4.	Ask for the price of an item and the quantity purchased. Display the amount of the total including GST.

#Ask for price of item
price = float(input ("Enter price: "))
#Ask for qty purchased
qty = int(input ("Enter quantity: "))
#Calculate SubTotal
subtotal = price * qty
#Calculate GST
gst = subtotal * .05
#Total
total = gst + subtotal
#display totals
print (f"Purchasing {qty} of this item worth ${price:.2f} including the GST amount of ${gst:.2f} is ${total:.2f}. ")
