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


def main():
    N, M = map(int, input().split())
    E = []
    for _ in range(M):
        a, b = map(int, input().split())
        E.append((a - 1, b - 1))

    res = 0
    for i in range(M):
        uf = UnionFind(N)
        # remove edge j
        for j in range(M):
            if i == j:
                continue
            uf.unite(E[j][0], E[j][1])

        # count groups
        n_groups = 0
        for x in range(N):
            if uf.root(x) == x:
                n_groups += 1

        if n_groups > 1:
            res += 1

    print(res)


main()
