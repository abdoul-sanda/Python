

import numpy as np


height = [1.22, 1.4, 2.7, 4.9, 6.8]
weight = [12, 15, 30, 50, 70]
numpy_height = np.array(height)
numpy_weight = np.array(weight)

bmi = numpy_weight / numpy_height ** 2 

print(f"Le BMI est : {bmi}")

