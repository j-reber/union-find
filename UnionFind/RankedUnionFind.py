class RankedUnionFind:
    def __init__(self, n):
        self.data = [-1 for i in range(n)]
        self.nr_blocks = n

    def rank_find(self, idx):
        tpl, tpu = 0, 0
        while self.data[idx] > 0:
            idx = self.data[idx]
            tpl += 1
        return idx, tpl, tpu

    def pc_ranked_find(self, idx):
        _, tpl, _ = self.rank_find(idx)
        tpu = 0
        org_idx = idx
        while self.data[idx] > 0:
            idx = self.data[idx]
        while self.data[org_idx] > 0:
            parent = self.data[org_idx]
            self.data[org_idx] = idx
            org_idx = parent
            tpu += 1
        return idx, tpl, tpu

    def ps_ranked_find(self, idx):
        _, tpl, _ = self.rank_find(idx)
        tpu = 0
        while self.data[idx] > 0:
            aux_idx = self.data[idx]
            self.data[idx] = self.data[self.data[idx]] if self.data[self.data[idx]] > 0 else self.data[idx]
            idx = aux_idx
            tpu += 1
        return idx, tpl, tpu

    def ph_ranked_find(self, idx):
        _, tpl, _ = self.rank_find(idx)
        tpu = 0
        while self.data[idx] > 0:
            self.data[idx] = self.data[self.data[idx]] if self.data[self.data[idx]] > 0 else self.data[idx]
            idx = self.data[idx]
            tpu += 1
        return idx, tpl, tpu

    def union_by_rank(self, i, j):
        ri, _, _ = self.rank_find(i)
        rj, _, _ = self.rank_find(j)
        if ri == rj:
            return
        if self.data[ri] >= self.data[rj]:
            self.data[rj] = min(self.data[rj], self.data[ri] - 1)
            self.data[ri] = rj
        else:
            self.data[rj] = ri
        self.nr_blocks -= 1

    def union_pc_by_rank(self, i, j):
        ri, _, _ = self.pc_ranked_find(i)
        rj, _, _ = self.pc_ranked_find(j)
        if ri == rj:
            return
        if self.data[ri] >= self.data[rj]:
            self.data[rj] = min(self.data[rj], self.data[ri] - 1)
            self.data[ri] = rj
        else:
            self.data[rj] = ri
        self.nr_blocks -= 1

    def union_ps_by_rank(self, i, j):
        ri, _, _ = self.ps_ranked_find(i)
        rj, _, _ = self.ps_ranked_find(j)
        if ri == rj:
            return
        if self.data[ri] >= self.data[rj]:
            self.data[rj] = min(self.data[rj], self.data[ri] - 1)
            self.data[ri] = rj
        else:
            self.data[rj] = ri
        self.nr_blocks -= 1

    def union_ph_by_rank(self, i, j):
        ri, _, _ = self.ph_ranked_find(i)
        rj, _, _ = self.ph_ranked_find(j)
        if ri == rj:
            return
        if self.data[ri] >= self.data[rj]:
            self.data[rj] = min(self.data[rj], self.data[ri] - 1)
            self.data[ri] = rj
        else:
            self.data[rj] = ri
        self.nr_blocks -= 1


if __name__ == '__main__':
    rf = RankedUnionFind(100)
    rf.union_by_rank(4, 5)
    rf.union_by_rank(6, 5)
    rf.union_by_rank(5, 3)
    rf.union_by_rank(7, 5)
    rf.union_by_rank(9, 5)
    rf.union_by_rank(5, 12)
    print(rf.data)

    print(rf.rank_find(4))
    print(rf.data)
    print(rf.nr_blocks)
