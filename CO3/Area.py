from Graphics.RectFunctions import *
from Graphics.CirFunctions import *
from Graphics.DGraphics.SphereFunctions import *
from Graphics.DGraphics.CuboidFunctions import *
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
print("Rectangle Area =",RectArea(l,b))
print("Rectangle Perimeter =",RectPerimeter(l,b))
r=int(input("Enter radius of the circle:"))
print("Circle Area =",CirArea(r))
print("Circle Perimeter =",CirPerimeter(r))
r=int(input("Enter radius of the sphere:"))
print("Sphere Area =",SpArea(r))
print("Sphere Volume =",SpPerimeter(r))
l=int(input("Enter cuboid length:"))
b=int(input("Enter cuboid breadth:"))
h=int(input("Enter cuboid height:"))
print("Cuboid Area =",CubArea(l,b,h))
print("Cuboid Perimeter =",CubPerimeter(l,b,h))      
