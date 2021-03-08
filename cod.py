class Friends:
  name = ""
  typ = ""
  def __init__(self,name,typ):
    self.name = name
    self.type = typ
    pass
  def __str__(self):
    return "Friend with name {} is very {}".format(self.name,self.type)
  def meet_friend(self):
    return "Friend with name {} meet with a new friend".format(self.name)
  
friend = Friends("Mishal","Sweet")
print(friend)

friend2 = Friends("Manish","nice")
print(friend2)



