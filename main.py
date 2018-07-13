#!/usr/bin/env python

import function

type = input("Calculation type: add/sub/multi/div ")
value1 = input("value1: ")
value2 = input("value2: ")

if type == "add": 
  result = function.calculate(value1,value2)
  print(result.addCal())
elif type == "sub":
  result = function.calculate(value1,value2)
  print(result.subCal())
elif type == "multi":
  result = function.calculate(value1,value2)
  print(result.multiCal())
elif type == "div":
  result = function.calculate(value1,value2)
  print(result.divCal())
else:
  print("byebye")
