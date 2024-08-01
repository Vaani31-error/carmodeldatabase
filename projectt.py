Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Cars:
...     brand = "Mahindra"
...     model = "XUV"
... 
...     def __init__(self, name, colour):
...         self.name = name
...         self.colour = colour
... 
...     def fun(self):
...         print("This is a newly launched car with CNG feature")
... 
... 
... car1 = Cars("breezze", "white")
... print(car1.brand,car1.model)
... print(car1.name, car1.colour)
