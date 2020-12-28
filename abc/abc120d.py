from itertools import combinations


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


def main():
    N, M = map(int, input().split())
    E = []
    for _ in range(M):
        a, b = map(int, input().split())
        E.append((a - 1, b - 1))

    res = []
    uf = UnionFind(N)
    inconv = N * (N - 1) // 2
    for i in range(M):
        res.append(inconv)
        a, b = E[M - 1 - i]
        root_a, root_b = uf.root(a), uf.root(b)
        size_a = uf.size[root_a]
        size_b = uf.size[root_b]
        uf.unite(a, b)
        if root_a == root_b:
            # inconv does not change
            continue

        inconv -= size_a * size_b
    print('\n'.join([str(v) for v in res[::-1]]))


main()
