fruit = {'mango','pineapple','orange','corn','tomato'}
vegetables = {'tomato','carrot','spinach','corn','cabbage'}
grains = {'wheat','rice','corn','barley'}

common_2 = fruit.intersection(vegetables)
common_3 = common_2.intersection(grains)
print("Commono items in three sets",common_3)

sd = fruit.symmetric_difference(vegetables).symmetric_difference(grains)
print(sd)

set_diff_1 = fruit-vegetables-grains
print(set_diff_1)

set_diff_2 = vegetables-fruit-grains
print(set_diff_2)

set_diff_3 = grains-fruit-vegetables
print(set_diff_3)