import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup


class MovieApp:
    def __init__(self, root, url):
        self.root = root
        self.url = url
        self.root.title("Movie Chart")

        # Treeview 위젯을 생성하고, 각 열의 제목을 설정합니다.
        self.tree = ttk.Treeview(root, columns=("Rank", "Title", "Admission Rate", "Release Date"), show="headings")
        self.tree.heading('Rank', text='순위')
        self.tree.heading('Title', text='영화 제목')
        self.tree.heading('Admission Rate', text='예매율')
        self.tree.heading('Release Date', text='개봉일')

        # 각 열의 너비를 설정합니다.
        self.tree.column('Rank', anchor=tk.CENTER, width=50)
        self.tree.column('Title', anchor=tk.W, width=200)
        self.tree.column('Admission Rate', anchor=tk.CENTER, width=100)
        self.tree.column('Release Date', anchor=tk.CENTER, width=100)

        # 스크롤바를 생성하고 Treeview 위젯에 연결합니다.
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Treeview 위젯과 스크롤바를 화면에 배치합니다.
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        # 웹 페이지로부터 데이터를 스크래핑하는 메서드를 호출합니다.
        self.scrape_movies()

    def scrape_movies(self):
        # 지정된 URL로부터 HTML을 가져옵니다.
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # 영화 정보를 담고 있는 태그를 찾아 반복 처리합니다.
            movies = soup.find_all('li', {'class': 'movieBox-item'})
            for index, movie in enumerate(movies, start=1):
                # 영화 제목을 추출합니다.
                title = movie.find('div', {'class': 'movie-title'}).find('h3').text.strip()
                # 예매율을 추출합니다.
                admission_rate = movie.find('li', {'class': 'ticketing'}).find('span').text.strip()
                # 개봉일을 추출합니다.
                release_date = movie.find('li', {'class': 'movie-launch'}).text.replace('개봉일', '').strip()

                # 추출한 정보를 Treeview 위젯에 추가합니다.
                self.tree.insert("", tk.END, values=(index, title, admission_rate, release_date))
        else:
            tk.messagebox.showerror("Error", "Failed to retrieve the webpage")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = MovieApp(root, 'https://m.moviechart.co.kr/rank/realtime/index/image')
    root.mainloop()

