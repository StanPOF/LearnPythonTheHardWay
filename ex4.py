# -*- coding: utf-8 -*-
cars = 100    
# 车车的总数
space_in_a_car = 4.0 
# 每辆车可以带四个人
drivers = 30 
# 有30个老司机
passengers = 90
# 有90个乘客
cars_not_driven = cars - drivers
# 不能跑的车＝车车总数－老司机
cars_driven = drivers
# 能跑的车＝老司机数量
carpool_capacity = cars_driven * space_in_a_car
# 乘客容量＝能跑的车＊每辆车的容量
average_passengers_per_car = passengers / cars_driven
# 平均每辆车的乘客数量＝乘客数量／能跑的车数量

print "There are", cars, "cars available."
# 车车总数
print "There are only", drivers, "drivers available."
# 老司机总数
print "There are will be", cars_not_driven, "empty cars today."
# 空车总数
print "We can transport", carpool_capacity, "people today."
# 今天能带多少个人呢
print "We have", passengers, "to carpool today."
# 今天要载多少个人呢
print "We need to put about", average_passengers_per_car, "in each car."
# 所以每辆车车要放几个人进去呢