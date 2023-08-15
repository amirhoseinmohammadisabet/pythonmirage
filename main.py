import numpy as np
import random

from equfunc import axbyz
from equfunc import devint

random_array = np.array([random.randint(1, 100) for _ in range(500)])

devint(random_array)
axbyz(5, 5, 5)
