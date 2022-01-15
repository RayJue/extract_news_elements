import re
import jieba
import zhconv
from opencc import OpenCC
cc = OpenCC('t2s')

def read(path):  # 读取txt文件，并返回list
        f = open(path, encoding="utf8")
        data = []
        for line in f.readlines():
            data.append(line)
        return data


def cht_to_chs_opencc(line):
    line = cc.convert(line)
    return line


def cht_to_chs_zhconv(line):
    line = zhconv.convert(line, 'zh-cn')
    return line


def remove_non_chinese(tokens):
    rst = []
    cn_reg = '^[\u4e00-\u9fa5]+$'

    for token in tokens:
        if re.search(cn_reg, token):
            rst.append(token)
    return rst


def cut_sentence(line):
    return jieba.cut(line.replace(' ', ''))


def cut_and_remove_non_chinese(line):
    tokens = jieba.cut(line.replace(' ', ''))
    tokens = remove_non_chinese(tokens)
    line_cut = ' '.join(tokens)
    return line_cut
