G = None
ans = None

def dfs(v, parent_c=-1, parent_id=-1):
    global G, ans
    k = 1
    for i in range(len(G[v])):
        edge_id, to = G[v][i]['edge_id'], G[v][i]['to']
        if to == parent_id: continue
        if k == parent_c: k+=1
        ans[edge_id] = k
        k += 1
        dfs(to, parent_c=ans[edge_id], parent_id=v)

def main():
    global G, ans
    N = int(input())
    G = [[] for _ in range(N)]
    ans = [0 for _ in range(N-1)]
    for edge_id in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append({'to': b, 'edge_id': edge_id})
        G[b].append({'to': a, 'edge_id': edge_id})
    
    dfs(0)
    print(max(ans))
    for a in ans:
        print(a)

main()