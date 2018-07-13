#!/usr/bin/env python

class calculate:
   def __init__ (self,a=0,b=0):
     self.cal1=a
     self.cal2=b

   def addCal(self):
     sum = float(self.cal1) + float(self.cal2)
     return sum
   
   def subCal(self):
     sub = float(self.cal1) - float(self.cal2)
     return sub

   def multiCal(self):
     mul = float(self.cal1) * float(self.cal2)
     return mul

   def divCal(self):
     div = float(self.cal1) / float(self.cal2)
     return div


