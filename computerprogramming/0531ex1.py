import math

def calculate_areas(radii):
    radiis = [float(r) for r in radii.split(",")]
    areas = [math.pi * r**2 for r in radiis]
    return areas


radii = input()
areas = calculate_areas(radii)
print(areas)
