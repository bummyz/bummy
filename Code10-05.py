import random

# 기본 설정: 원본 2차원 리스트의 크기, 새로운 리스트를 시작할 위치, 새로운 리스트의 크기
SIZE = 5   # 원본 2차원 리스트의 크기는 5x5입니다.
startRow, startCol = 1, 1   # 새로운 리스트를 추출할 시작 위치는 (1, 1)입니다.
nSIZE = 3   # 새로운 리스트의 크기는 3x3입니다.

# 파이썬으로 2차원 리스트를 생성합니다.
value = 1
myList1 = []
for _ in range(SIZE):
    tmpList = []  # 임시 리스트를 만들어 각 행을 구성합니다.
    for _ in range(SIZE):
        tmpList.append(value)  # 각 행에 1부터 순서대로 값을 추가합니다.
        value += 1  # 다음 값으로 증가시킵니다.
    myList1.append(tmpList)  # 완성된 행을 원본 리스트에 추가합니다.

# 원본 2차원 리스트를 출력합니다.
for i in range(SIZE):
    [print("%3d" % myList1[i][k], end=' ') for k in range(SIZE)]
    print()  # 각 행을 출력한 후에 줄바꿈을 합니다.
print()

# 파이썬 2차원 리스트를 슬라이싱하여 새로운 리스트를 만듭니다.
myList2 = []
for i in range(startRow, startRow + nSIZE):
    tmpList = []  # 새로운 리스트를 위한 임시 행을 만듭니다.
    for k in range(startCol, startCol + nSIZE):
        tmpList.append(myList1[i][k])  # 지정된 위치부터 nSIZE 만큼 값을 임시 행에 추가합니다.
    myList2.append(tmpList)  # 완성된 임시 행을 새로운 리스트에 추가합니다.

# 새로운 2차원 리스트를 출력합니다.
for i in range(nSIZE):
    [print("%3d" % myList2[i][k], end=' ') for k in range(nSIZE)]
    print()  # 각 행을 출력한 후에 줄바꿈을 합니다.
print()
