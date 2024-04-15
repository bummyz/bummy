import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup


class MovieApp:
    def __init__(self, root, url):
        self.root = root
        self.url = url
        self.root.title("Movie Chart")

        # Treeview 위젯 생성 및 설정
        self.tree = ttk.Treeview(root, columns=("Rank", "Title"), show="headings")
        self.tree.heading('Rank', text='순위')
        self.tree.heading('Title', text='영화 제목')
        self.tree.column('Rank', anchor=tk.CENTER, width=100)
        self.tree.column('Title', anchor=tk.W, width=300)

        # 스크롤바 생성 및 설정
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # 위젯 배치
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        # 스크래핑 실행
        self.scrape_movies()

    def scrape_movies(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # 영화 제목을 찾습니다. 클래스 이름은 실제 사이트 구조에 맞게 수정해야 합니다.
                movie_titles = soup.find_all('div', {'class': 'movie-title'})
                for index, title in enumerate(movie_titles, start=1):
                    self.tree.insert("", tk.END, values=(index, title.text.strip()))
            else:
                tk.messagebox.showerror("Error", "Failed to retrieve the webpage")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = MovieApp(root, 'https://m.moviechart.co.kr/rank/realtime/index/image')  # 실제 작동하는 URL로 변경 필요
    root.mainloop()
