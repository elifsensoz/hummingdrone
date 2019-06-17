def fib(n): 
    if n>=0: 
      if n==0:
        return 0
      elif n==1: 
          return 1
      else: 
          return fib(n-1)+fib(n-2)
    else:
      print("Incorrect number")
      return -1

class UAV:

    # Class attribute
    # name (data type: string)
    # is_landing (data type: boolean, default False)
    # is_takeoff (data type: boolean, default False)
    name = ""
    is_landing = False
    is_takeoff = False 

    # Initializer / Instance attributes
    


    # instance method
    def takeoff(self):
        pass

# Child class (inherits from Dog class)
class Drone(UAV):
    def __init__(self, name):
        self.name = name

    def takeoff(self):
      if(self.is_landing):
        return False
      else:
        is_takeoff = True
        return is_takeoff


if __name__ == '__main__':
  print(fib(6))

