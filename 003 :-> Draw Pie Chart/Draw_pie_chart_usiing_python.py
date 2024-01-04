#pip install matplotlib
from cProfile import label
import matplotlib.pyplot as p
s = [40,30,10,10,10]
i = ["Python","Java","C++","C","Javascript"]
p.pie(s,label=i)
p.show()
