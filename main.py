import hashlib

# не изменяйте это значение
TARGET = "3c8aed7d3d1699163349850b93014642"

def main():
    i = 0
    while i < 2147483647:
        digest = hashlib.md5(str(i).encode()).hexdigest()
        if digest == TARGET:
            print(f"Найдено: {l}")
            return

if __name__ == "__main__":
    main()