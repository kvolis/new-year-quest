import hashlib

# не изменяйте эти значение
TARGET_START = "e8c48234fd"
TARGET_END = "d2e3e0c962"


def main():
    i = 0
    while i < 2147483647:

        digest = hashlib.md5(str(i).encode()).hexdigest()

        if digest.startswith(TARGET_START) and digest.endswith(TARGET_END):
            print(f"Найдено: {l}")
            return

if __name__ == "__main__":
    main()