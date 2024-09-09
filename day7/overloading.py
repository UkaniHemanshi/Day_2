class calculator:
    def add(self,*args):
        return sum(args)
cal = calculator()
print(cal.add(1,2,3))
print(cal.add(1,2,3,4))