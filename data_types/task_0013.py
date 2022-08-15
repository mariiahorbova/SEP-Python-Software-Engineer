# 13. Write a Python program which accepts the radius of the sphere as input and compute the volume.
# Sample Output:
# Input the radius of the circle: The volume of the sphere is: 392.699081625.
from math import pi

def sphere_volume(radius):
    return 4/3 * pi * radius ** 3


print(sphere_volume(3))
print(sphere_volume(17))
