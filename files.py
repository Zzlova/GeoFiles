import os


def main():
    lf = list_files("2020-03-12T10-20-51_4")
    num = len(lf)
    print("Количество файлов: ", num)
    for i in range(0, num):
        print(os.path.splitext(lf[i])[1])


def list_files(path):
    lf = os.listdir(path)
    return lf


main()
