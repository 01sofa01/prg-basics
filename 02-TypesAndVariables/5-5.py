price= float(input('Enter price:'))
discount= int(input('Enter discount %:'))
price_with_discount= float(price)-(price)*(discount)/100
reduction= ((price)-(price_with_discount))
print(f'Product price is {price}. The discount is {discount}. Discounted price is {price_with_discount: .2f}. Reduction is {reduction: .2f}.')
