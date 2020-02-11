Last editted by: Angeline Hidalgo
Editted on: Februrary 9, 2020

# Prompts user to enter their current time in hours.
currentTimeStr = input("What is the current time (in hours 0-23)?")
# Prompts user to enter how many hours they want to wait.
waitTimeStr = input("How many hours do you want to wait?")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

# Prints out the expected final time with the equation provided for 'finalTimeInt'.
finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)
