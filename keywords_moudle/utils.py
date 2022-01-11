def read(path):  # 读取txt文件，并返回list
        f = open(path, encoding="utf8")
        data = []
        for line in f.readlines():
            data.append(line)
        return data