import os
import subprocess

def main():
    url = input("Введите ссылку на YouTube-видео: ").strip()
    save_path = input("Введите путь для сохранения (по умолчанию текущая папка): ").strip()

    if not save_path:
        save_path = os.getcwd()

    try:
        print("Скачивание видео...")
        subprocess.run([
            "yt-dlp",
            "-P", save_path,
            url
        ])
        print("Скачивание завершено.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
