lst1 = [8, 19, 148, 4]
lst2 = [9, 1, 33, 83]

product_lst = []

for n in lst1:
	for m in lst2:
		product = n * m
		print(product)
		product_lst.append(product)