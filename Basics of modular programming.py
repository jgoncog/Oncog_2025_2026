#This code is made by: Josue Ruch III "Thirdy" G. Oncog
def marathon_time(speed):
      distance = 42.195
      time = distance / speed
      hours = int(time)
      minutes = int((time - hours) * 60)
      return hours, minutes

speed = float(input("Enter speed (km/h): "))
hours,minutes = marathon_time(speed)
print(f"Time: {hours} hours, {minutes} minutes")

#What is the purpose of this function you created?
#1.The purpose of this function is to calculate how long it takes for a marathon runner to complete a race. It demonstrates the applications and use of global and local variables.

#2.Identify which variables are global and which are local in your code.
#Local variables- distance,time,hours, and minutes.
#Global variables - speed is an example of a global variable.

#Why is variable scope important?
#3. For one, this can help us keep things organized in our code by reducing the risk of naming conflicts. To add, this can also prevent errors. For example,local variables are only accessible within their function, protecting them from any changes made outside their function.

 