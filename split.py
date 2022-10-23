#划分训练、验证和测试集

import numpy as np


def read_elements():
    # file_path = "E:/pythonProject/fusion/ceshi.txt"
    # fp = open(file_path)
    # lines = fp.readlines()
    #
    # file_path_test = "E:/pythonProject/fusion/ceshi1"
    # fp1 = open(file_path_test)
    # lines_quchu = fp1.readlines()
    #
    #
    #
    # for line1 in lines_quchu:
    #     for line in lines:
    #         if line1 in line:
    #             continue
    #         fw = open('E:/pythonProject/fusion/train_new.txt', 'a')
    #         fw.write(line)
    def isInArray(file, line):
        for item in file:
            if item in line:
                return True
        return False

    if __name__ == '__main__':

        file_path_test = "C://Users\wsco28\Desktop\super_node\FB15K237\FB15K237\Hypernode/except.txt"
        fp1 = open(file_path_test)
        lines_quchu = fp1.readlines()

        with open('C://Users\wsco28\Desktop\super_node\FB15K237\FB15K237//all//train.txt', 'r') as f:
            with open('C://Users\wsco28\Desktop\super_node\FB15K237\FB15K237//all/train_new.txt', 'w') as g:
                for line in f.readlines():
                    if not isInArray(lines_quchu, line):
                        g.write(line)


if __name__ == '__main__':

    read_elements()