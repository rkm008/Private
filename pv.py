import os
import random
import shutil
from datetime import datetime

# ANSI color codes
colors = [
    "\033[1;31m",  # Red
    "\033[1;32m",  # Green
    "\033[1;33m",  # Yellow
    "\033[1;34m",  # Blue
    "\033[1;35m",  # Magenta
    "\033[1;36m",  # Cyan
]

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")
    print()
    print()

def banner():
    clear_screen()
    color = random.choice(colors)
    width = shutil.get_terminal_size().columns
    ascii_lines = [
        "▗▄▄▖ ▗▄▄▖ ▗▄▄▄▖▗▖  ▗▖ ▗▄▖▗▄▄▄▖▗▄▄▄▖",
        "▐▌ ▐▌▐▌ ▐▌  █  ▐▌  ▐▌▐▌ ▐▌ █  ▐▌    ",
        "▐▛▀▘ ▐▛▀▚▖  █  ▐▌  ▐▌▐▛▀▜▌ █  ▐▛▀▀▘",
        "▐▌   ▐▌ ▐▌▗▄█▄▖ ▝▚▞▘ ▐▌ ▐▌ █  ▐▙▄▄▖",
        "",
    ]
    print(color)
    for line in ascii_lines:
        print(line.center(width))
    print("=" * width)
    print("R. K. M. PRIVATE".center(width))
    print("=" * width + "\033[0m")  # Reset color
    print()
    print()

def download_video():
    video_url = input("Enter your video link: ").strip()

    if not video_url.startswith("http"):
        print("❌ Invalid URL. It must start with http or https.")
        return

    if not os.path.exists("cookies.txt"):
        print("❌ 'cookies.txt' file not found in this directory.")
        return

    print("\n📥 Downloading in best video and audio...\n")

    now = datetime.now()
    filename = now.strftime("%S-%H-%d-%m-%Y")

    command = f'yt-dlp --cookies cookies.txt -f "bestvideo+bestaudio/best" -o "{filename}.%(ext)s" "{video_url}"'
    os.system(command)

def main():
    while True:
        banner()
        download_video()
        again = input("\n📥 Do you want to download another video? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Exiting. Thank you!")
            break

if __name__ == "__main__":
    main()