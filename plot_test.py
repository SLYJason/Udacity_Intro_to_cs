#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
y = [20,10,30,25,15]
index = np.arange(5)
plt.bar(left=index, height=y, color='green', width=0.5)
plt.show()
