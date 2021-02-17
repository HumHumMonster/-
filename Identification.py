import math
import os
from Characteristic_value import get_all_eigen_b


# 求向量点积
def add_vectors(a, b):
    res = 0
    for i in range(len(a)):
        res += float(a[i]) * float(b[i])
    return res


# 求向量的模
def module_vectors(a):
    return math.sqrt(sum([float(x) ** 2 for x in a]))


# 求向量夹角余弦值
def get_cos(a, b):
    add_a, add_b = module_vectors(a), module_vectors(b)
    if add_a != 0 and add_b != 0:
        return add_vectors(a, b) / (add_a * add_b)
    return 0


divide_path = "divide/"


def identify(now_image):
    now_vector = get_all_eigen_b(now_image)

    res_val = 0
    res_key = "Null"

    for key in os.listdir(divide_path):
        fp = open(divide_path + key + "/vectors.txt", "r")  # 读取
        test_all_vector = fp.read().split()
        test_vector = []
        for i in range(len(test_all_vector)):
            if i % 17 == 0:
                now_val = get_cos(test_vector, now_vector)
                if now_val > res_val:
                    res_val = now_val
                    res_key = key
                test_vector = []
            test_vector.append(test_all_vector[i])
    return res_key