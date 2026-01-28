import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__)) 


def fetch_github_data():

    username = entry.get().strip()

    if not username:
        messagebox.showerror("Ошибка", "Введите имя пользователя GitHub")
        return

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            messagebox.showerror(
                "Ошибка",
                "Пользователь не найден"
            )
            return

        data = response.json()

        result = {
            "company": data.get("company"),
            "created_at": data.get("created_at"),
            "email": data.get("email"),
            "id": data.get("id"),
            "name": data.get("name"),
            "url": data.get("url")
        }

        # запись в JSON
        file_path = os.path.join(script_dir, "get_github_data.json")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent = 4, ensure_ascii = False)

        messagebox.showinfo(
            "Выполнено!",
            "Данные успешно сохранены в файл get_github_data.json"
        )

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка сети", str(e))


root = tk.Tk()
root.title("Парсер данных в формате JSON")
root.geometry("400x200")

label = tk.Label(
    root,
    text = "Введите имя пользователя GitHub:",
    font = ("Segoi UI", 12)
)
label.pack(pady = 10)

entry = tk.Entry(root, width = 30, font = ("Arial", 12))
entry.pack(pady = 5)

button = tk.Button(
    root,
    text="Получить данные",
    command = fetch_github_data,
    font=("Segoi UI", 12)
)
button.pack(pady = 20)

root.mainloop()