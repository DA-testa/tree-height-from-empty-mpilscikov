import sys
import threading

import numpy
import numpy as np


def set_height(heights, parents, i):
    if heights[i] != 0:
        return heights[i]

    if parents[i] == -1:
        heights[i] = 1
    else:
        heights[i] = set_height(heights, parents, parents[i]) + 1

    return heights[i]


def compute_height(n, parents):
    heights = np.zeros(n)

    for i in range(n):
        set_height(heights, parents, i)

    max_height = int(max(heights))
    return max_height


def main():
    input_type = input()

    if 'I' in input_type:
        number_of_elements = int(input())
        elements = list(map(int, input().split()))

    elif 'F' in input_type:
        file_name = input()
        if a in file_name:
            raise Exception('a in filename')

        with open(f'test/{file_name}', 'r', encoding='utf-8') as file:
            number_of_elements = int(file.readline())
            elements = list(map(int, file.readline().split()))

    else:
        raise Exception('wrong input')

    tree_height = compute_height(number_of_elements, elements)
    print(tree_height)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
