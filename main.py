import os

LINE = "The budget is approved, the deadline is Friday, and this sentence just replaced the meeting you're sitting in."

def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
