print("Chapter 1 Exercises")
print("-------------------")
print("My only comment - The hardest part of this whole assignment was getting everything installed and setup correctly.")
print()
print("Number 2")
print("No it is not. It can appear to be but belong to a different distribution.")
print()

print("Number 3")
print("when the data has outliers")
print()

print("Number 4")
import random
random.seed(0)
salaries = [round(random.random()*1000000, -3) for _ in range(100)]
print(salaries)
print()

print("Number 5")
from statistics import mean
sum(salaries) / len(salaries) == mean(salaries)
print("A. mean:",mean(salaries))

import math
def find_median(x):
    x.sort()
    midpoint = (len(x) + 1) / 2 - 1
    if len(x) % 2:
        return x[int(midpoint)]
    else:
        return (x[math.floor(midpoint)] + x[math.ceil(midpoint)]) / 2
from statistics import median
find_median(salaries) == median(salaries)
print("B. median:",find_median(salaries))

from statistics import mode
from collections import Counter
Counter(salaries).most_common(1)[0][0] == mode(salaries)
print("C. mode:",mode(salaries))

from statistics import variance
sum([(x - sum(salaries) / len(salaries))**2 for x in salaries]) / (len(salaries) - 1) == variance(salaries)
print("D. sample variance:",variance(salaries))

from statistics import stdev
import math
math.sqrt(sum([(x - sum(salaries) / len(salaries))**2 for x in salaries]) / (len(salaries) - 1)) == stdev(salaries)
print("E. sample standard deviation:",stdev(salaries))

print()
print("Number 6")
print("A. range:",max(salaries) - min(salaries))
from statistics import mean, stdev
print("B. coeff of variation",stdev(salaries) / mean(salaries))
import math
def quantile(x, pct):
    x.sort()
    index = (len(x) + 1) * pct - 1
    if len(x) % 2:
        return x[int(index)]
    else:
        return (x[math.floor(index)] + x[math.ceil(index)]) / 2
sum([x < quantile(salaries, 0.25) for x in salaries]) / len(salaries) == 0.25
sum([x < quantile(salaries, 0.75) for x in salaries]) / len(salaries) == 0.75
q3, q1 = quantile(salaries, 0.75), quantile(salaries, 0.25)
iqr = q3 - q1
print("C. interquartile range",iqr)
print("D. quartile coeff of dispersion",iqr / (q1 + q3))
print()

print("Number 7")
min_salary, max_salary = min(salaries), max(salaries)
salary_range = max_salary - min_salary
min_max_scaled = [(x - min_salary) / salary_range for x in salaries]
min_max_scaled[:5]
print("A. min-max scaling:",min_max_scaled[:5])

from statistics import mean, stdev
mean_salary, std_salary = mean(salaries), stdev(salaries)
standardized = [(x - mean_salary) / std_salary for x in salaries]
print("B. standardizing:",standardized[:5])
print()

print("Number 8")
import numpy as np
np.cov(min_max_scaled, standardized)
from statistics import mean
running_total = [
    (x - mean(min_max_scaled)) * (y - mean(standardized))
    for x, y in zip(min_max_scaled, standardized)
]
cov = mean(running_total)
print("A. covariance btwn stand and norm data:",cov)

from statistics import stdev
pcoeff=cov / (stdev(min_max_scaled) * stdev(standardized))
print("B. pearson coeff",pcoeff)
