import sys
from typing import Union
sys.setrecursionlimit(1 << 20)
INF = float('inf')


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


import copy


class UnionFind:
    def __init__(self, size, val) -> None:
        self.parent = [-1] * size
        self.size = [1] * size
        self.members = [[i] for i in range(size)]
        self.val = copy.copy(val)

    def root(self, x: int) -> int:
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        # print('unite', x, y, 'val', self.val)
        x_root = self.root(x)
        y_root = self.root(y)
        if x_root == y_root:  # already same group
            return False

        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
            self.val[y_root] += self.val[x_root]
            self.members[y_root] += self.members[x_root]
            # print(self.val[y_root], '+=', self.val[x_root])
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.val[x_root] += self.val[y_root]
            self.members[x_root] += self.members[y_root]
            # print(self.val[x_root], '+=', self.val[x_root])
        return True

    def print(self):
        print('----')
        print('parent', self.parent)
        print('size  ', self.size)
        print('vals  ', self.val)
        print('members  ', self.members)


def main():
    N, M = read_ints()
    A = read_int_list()
    B = read_int_list()
    uf = UnionFind(N, A)
    for _ in range(M):
        c, d = read_ints()
        c -= 1
        d -= 1
        uf.unite(c, d)
    # uf.print()

    for v in range(N):
        if uf.parent[v] == -1:
            members = uf.members[v]
            a_sum = sum([A[i] for i in members])
            b_sum = sum([B[i] for i in members])
            # print('members', members, a_sum, b_sum)
            if a_sum != b_sum:
                print('No')
                return
    print('Yes')


main()
