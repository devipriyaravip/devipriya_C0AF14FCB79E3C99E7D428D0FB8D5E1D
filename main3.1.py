def  linearsearchproduct(productList,targetproduct):
  indices=[]
  for index,product in enumerate(productList):
   if product == targetproduct:
     indices . append (index)
  return indices
#Example usage:
product =["shoes","boot","loafer","shoes","sandal","shoes"]
target ="shoes"
result = linearsearchproduct(product,target)
print(result)