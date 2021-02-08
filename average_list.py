def calc_average(list1):
   length = len(list1)
   if length == 0:
      return 0
   result = 0
   for i in list1:
      result = result + i
   result = result / length
   return result
