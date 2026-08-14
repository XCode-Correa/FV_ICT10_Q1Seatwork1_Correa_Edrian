# Seatwork 1
from pyscript import display, document

fullname = "Edrian Correa"  # string
age1 = 15   # integer
height1 = 177.8     # floating-point/float
student_type = False    # boolean
bucket_countries = ["Japan", "Germany", "Italy"]    # list
favorite_stuff = {"Color":'White/Black', "Car_brand":'BMW, Ferrari, Porsche', "Shoe_size":'US 12-13', "Best_friends":'Sean, Ynigo, Diego, Dylan, Matt'}     # dictionary
fav_fruits = {"Banana", "Apple", "Orange", "Melon", "Coconut"}
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

display(f"Name: {fullname}", target="name")
display(f"Age: {age1}", target="age")
display(f"Height: {height1}", target="height")
display(f"Is new student: {student_type}", target="student")
display(f"Countries to visit: {bucket_countries}", target="bucket_countries")
display(f"Others: {favorite_stuff}", target="fav_stuff")
display(f"Fruits: {fav_fruits}", target="fav_fruits")
display(f"Days of the week: {days_of_week}", target="days_week")