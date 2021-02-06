import sys
sys.setrecursionlimit(1 << 20)
INF = float('inf')


class UnionFind:
    def __init__(self, size) -> None:
        self.parent = [-1] * size
        self.size = [1] * size

    def root(self, x: int) -> int:
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        x_root = self.root(x)
        y_root = self.root(y)
        if x_root == y_root:  # already same group
            return False

        if self.size[x_root] < self.size[y_root]:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]
        else:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        return True

    def print(self):
        print('----')
        print('parent', self.parent)
        print('size  ', self.size)


def read_int_list():
    return list(map(int, input().split()))


def read_ints():
    return map(int, input().split())


def main():
    N, M = read_ints()
    uf = UnionFind(N)
    for _ in range(M):
        a, b = read_ints()
        a -= 1
        b -= 1
        uf.unite(a, b)
    # uf.print()
    print(max(uf.size))


main()
