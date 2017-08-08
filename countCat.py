def isCat():
  """True if the animal is a cat"""
  print("***Checking if this is a cat***")
  animal = input("Input your animal here:")
  if (animal == "cat"):
    return True
  else:
    return False
def countCat():
  """Count how many cats do we have
     End program if animal is not cat"""
  print("***Counting how many cats***")
  catNum = 0
  while (isCat() == True):
    catNum = catNum+1
    print("Meow~")
  return catNum

print(countCat())


  
