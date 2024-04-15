# 필요한 라이브러리를 임포트합니다.
import numpy as np  # NumPy 라이브러리를 np라는 이름으로 임포트합니다.
import random  # 난수 생성을 위해 random 라이브러리를 임포트합니다.

# 0에서 255 사이의 난수 5개를 포함하는 파이썬 리스트를 생성합니다.
pythonList = [random.randint(0, 255) for _ in range(5)]
# 생성된 파이썬 리스트를 출력합니다.
print('* 파이썬 리스트 --> ', pythonList)

# 파이썬 리스트를 NumPy 배열로 변환합니다.
numpyAry1 = np.array(pythonList)
# 변환된 NumPy 배열을 출력합니다.
print('* array(pythonList) --> ', numpyAry1)

# 0부터 시작하여 5미만의 정수로 이루어진 NumPy 배열을 생성합니다.
numpyAry2 = np.arange(5)
# 생성된 배열을 출력합니다.
print('* arange(5) --> ', numpyAry2)

# 3부터 시작하여 8미만의 정수로 이루어진 NumPy 배열을 생성합니다.
numpyAry3 = np.arange(3, 8)
# 생성된 배열을 출력합니다.
print('* arange(3, 8) --> ', numpyAry3)

# 모든 요소가 1인 길이가 5인 NumPy 배열을 생성합니다.
numpyAry4 = np.ones(5)
# 생성된 배열을 출력합니다.
print('* ones(5) --> \n', numpyAry4)

# 모든 요소가 1인 3x4 크기의 2차원 NumPy 배열을 생성합니다.
numpyAry5 = np.ones((3, 4))
# 생성된 2차원 배열을 출력합니다.
print('* ones((3,4)) )--> \n', numpyAry5)

# 모든 요소가 0인 길이가 5인 NumPy 배열을 생성합니다.
numpyAry6 = np.zeros(5)
# 생성된 배열을 출력합니다.
print('* zeros(5) --> ', numpyAry6)

# 초기화되지 않은 값으로 구성된 길이가 6인 NumPy 배열을 생성합니다.
# `empty` 함수로 생성된 배열의 요소는 예측할 수 없으며, 메모리 상태에 따라 달라집니다.
numpyAry7 = np.empty(6)
# 생성된 배열을 출력합니다.
print('* empty(6) --> ', numpyAry7)

# 모든 요소가 33인 길이가 5인 NumPy 배열을 생성합니다.
numpyAry8 = np.full(5, 33)
# 생성된 배열을 출력합니다.
print('* full(5, 33) --> ', numpyAry8)

# 5x5 크기의 단위 행렬(Identity Matrix)을 생성합니다.
# 단위 행렬은 주대각선 요소가 모두 1이고, 나머지 요소는 0인 정사각 행렬입니다.
numpyAry9 = np.identity(5)
# 생성된 단위 행렬을 출력합니다.
print('* identity(5) --> \n', numpyAry9)

