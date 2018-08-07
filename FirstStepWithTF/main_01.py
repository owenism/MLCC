"""
Quick Introduction to pandas.
pandas is an important library for data analysis and modeling, and is widely used in TensorFlow coding.
This tutorial provides all the pandas information you need for this course. If you already know pandas,
you can skip this exercise.
"""

import pandas as pd

#print(pd.__version__)


city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = ([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })
# DataFrame 객체는 argument로 dict 자료형을 넘겨 만들 수 있다.
