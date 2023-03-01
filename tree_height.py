import sys
import threading

import numpy as np


def populate_tree_array(n, parents):
    tree = np.zeros((n, n), dtype=int)

    for i in range(n):
        if parents[i] != -1:
            tree[parents[i], i] = 1
            tree[i, parents[i]] = 1

    return tree


def get_tree_height(root, n, parents, tree):
    if not np.sum(tree[root]):
        return 1

    height = 0
    for i in range(n):
        if tree[root, i] and parents[root] != i:
            height = max(height, get_tree_height(i, n, parents, tree))

    return height + 1


def compute_height(n, parents):
    tree = populate_tree_array(n, parents)
    root = parents.index(-1)
    max_height = get_tree_height(root, n, parents, tree)

    return max_height


def main():
    input_type = input()

    if input_type == 'I':
        number_of_elements = int(input())
        elements = list(map(int, input().split()))

    elif input_type == 'F':
        file_name = input()

        with open(file_name, 'r', encoding='utf-8') as file:
            rows = file.readlines()

            number_of_elements = int(rows[0].replace('\n', ''))
            elements = list(map(int, input().replace('\n', '').split()))

    tree_height = compute_height(number_of_elements, elements)
    print(tree_height)


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
