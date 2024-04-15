# 필요한 모듈을 임포트합니다.
import sqlite3
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##

# 데이터를 데이터베이스에 삽입하는 함수입니다.
def insertData():
    # 데이터베이스 연결과 커서 객체 초기화
    con, cur = None, None
    # 사용자 입력 데이터를 저장할 변수 초기화
    data1, data2, data3, data4 = "", "", "", ""

    # 데이터베이스 연결
    con = sqlite3.connect('/Users/bummy/bummydatabase.db')
    cur = con.cursor()

    # 사용자로부터 입력 받은 데이터
    data1 = edt1.get(); data2 = edt2.get(); data3 = edt3.get(); data4 = edt4.get()
    try:
        # 삽입할 데이터를 SQL 문에 포함시킴 (파라미터 사용 권장)
        sql = "INSERT INTO userTable VALUES (?, ?, ?, ?)"
        cur.execute(sql, (data1, data2, data3, data4))
    except Exception as e:
        # 데이터 삽입 시 오류 발생하면 오류 메시지를 표시
        messagebox.showerror('오류', '데이터 입력 오류가 발생함: ' + str(e))
    else:
        # 데이터 삽입 성공 시 메시지 표시
        messagebox.showinfo('성공', '데이터 입력 성공')
    # 데이터베이스에 변경사항을 커밋하고 연결을 닫음
    con.commit()
    con.close()

# 데이터베이스에서 데이터를 조회하여 표시하는 함수입니다.
def selectData():
    # 조회된 데이터를 저장할 리스트 초기화
    strData1, strData2, strData3, strData4 = [], [], [], []
    # 데이터베이스 연결
    con = sqlite3.connect('/Users/bummy/bummydatabase.db')
    cur = con.cursor()
    # userTable에서 모든 데이터를 조회
    cur.execute("SELECT * FROM userTable")

    # 컬럼명 추가
    strData1.append("사용자ID"); strData2.append("사용자이름")
    strData3.append("이메일"); strData4.append("출생연도")
    # 구분선 추가
    strData1.append("-----------"); strData2.append("-----------")
    strData3.append("-----------"); strData4.append("-----------")

    # 조회된 모든 행을 반복하여 리스트에 추가
    while True:
        row = cur.fetchone()
        if row == None:
            break
        strData1.append(row[0]); strData2.append(row[1])
        strData3.append(row[2]); strData4.append(row[3])

    # Listbox의 기존 데이터를 삭제
    listData1.delete(0, END); listData2.delete(0, END)
    listData3.delete(0, END); listData4.delete(0, END)
    # 조회된 데이터를 Listbox에 추가
    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1); listData2.insert(END, item2)
        listData3.insert(END, item3); listData4.insert(END, item4)
    # 데이터베이스 연결 닫기
    con.close()

## 메인 코드 부분 ##
# Tkinter 윈도우 생성
window = Tk()
window.geometry("600x300")  # 윈도우 크기 설정
window.title("GUI 데이터 입력")  # 윈도우 타이틀 설정

# Entry 위젯을 포함할 프레임 생성 및 배치
edtFrame = Frame(window)
edtFrame.pack()

# Listbox 위젯을 포함할 프레임 생성 및 배치
listFrame = Frame(window)
listFrame.pack(side = BOTTOM, fill = BOTH, expand = 1)

# 사용자 입력을 받을 Entry 위젯 생성 및 배치
edt1 = Entry(edtFrame, width = 10); edt1.pack(side = LEFT, padx = 10, pady = 10)
edt2 = Entry(edtFrame, width = 10); edt2.pack(side = LEFT, padx = 10, pady = 10)
edt3 = Entry(edtFrame, width = 10); edt3.pack(side = LEFT, padx = 10, pady = 10)
edt4 = Entry(edtFrame, width = 10); edt4.pack(side = LEFT, padx = 10, pady = 10)

# 데이터 입력 및 조회를 위한 버튼 생성 및 배치
btnInsert = Button(edtFrame, text = "입력", command = insertData)
btnInsert.pack(side = LEFT, padx = 10, pady = 10)
btnSelect = Button(edtFrame, text = "조회", command = selectData)
btnSelect.pack(side = LEFT, padx = 10, pady = 10)

# 조회 결과를 표시할 Listbox 위젯 생성 및 배치
listData1 = Listbox(listFrame, bg = 'yellow')
listData1.pack(side = LEFT, fill = BOTH, expand = 1)
listData2 = Listbox(listFrame, bg = 'yellow')
listData2.pack(side = LEFT, fill = BOTH, expand = 1)
listData3 = Listbox(listFrame, bg = 'yellow')
listData3.pack(side = LEFT, fill = BOTH, expand = 1)
listData4 = Listbox(listFrame, bg = 'yellow')
listData4.pack(side = LEFT, fill = BOTH, expand = 1)

# Tkinter 이벤트 루프 시작
window.mainloop()
