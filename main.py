initial_earth_weight = float(input("请输入您在地球上的初始体重（kg）："))
lunar_ratio = 0.165
print("未来10年地球和月球体重变化：")
print("年份\t地球体重(kg)\t月球体重(kg)")
for year in range(1, 11):
    earth_weight = initial_earth_weight + year * 0.5
    lunar_weight = earth_weight * lunar_ratio
    print(f"{year}\t{earth_weight:.2f}\t\t{lunar_weight:.2f}")# 在这个文件里编写代码
