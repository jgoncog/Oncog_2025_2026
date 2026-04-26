import math

#ask te user for input

launche_angle_degrees = float(input("Enter launch angle ( in degrees): ") )


max_horizontal_distance =  float(input("Enter the maximum horizontal distance(meters) : ") )


gravity = 9.8

launche_angle_radians = math.radians(launche_angle_degrees)  

velocity = math.sqrt((max_horizontal_distance * gravity)/math.sin(2*launche_angle_radians ))

print (f"Required launch speed: {velocity:.2f} m/s")