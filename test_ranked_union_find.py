from itertools import combinations
import random
import matplotlib.pyplot as plt
from UnionFind.RankedUnionFind import RankedUnionFind

random.seed(0)

if __name__ == '__main__':
    n = 10000  # 5000, 10000
    delta = 1
    avg_tpl_nc, avg_tpu_nc, idx_nc = [], [], []
    avg_tpl_pc, avg_tpu_pc, idx_pc = [], [], []
    avg_tpl_ps, avg_tpu_ps, idx_ps = [], [], []
    avg_tpl_ph, avg_tpu_ph, idx_ph = [], [], []

    lst = [n for n in range(n)]
    comb = list(combinations(lst, 2))
    random.shuffle(comb)
    ruf_nc = RankedUnionFind(n)
    ruf_pc = RankedUnionFind(n)
    ruf_ps = RankedUnionFind(n)
    ruf_ph = RankedUnionFind(n)

    # Analyze tpu and tpl with no compression
    for i, pair in enumerate(comb):
        print(1, i)
        ruf_nc.union_by_rank(pair[0], pair[1])
        if ruf_nc.nr_blocks == 1:
            # Abort the queue once there is only one block left
            break
        if i % delta == 0:
            # Get average TPL and TPU after delta unions
            sum_tpu, sum_tpl = 0, 0
            for j in range(n):
                _, tpl, tpu = ruf_nc.rank_find(j)
                sum_tpu += tpu
                sum_tpl += tpl

            # print(sum_tpu / n, sum_tpl / n)
            avg_tpl_nc.append(sum_tpl / n)
            avg_tpu_nc.append(sum_tpu / n)
            idx_nc.append(i)

    # Do the same thing for full pc
    for i, pair in enumerate(comb):
        print(2, i)
        ruf_pc.union_by_rank(pair[0], pair[1])
        if ruf_pc.nr_blocks == 1:
            # Abort the queue once there is only one block left
            break
        if i % delta == 0:
            # Get average TPL and TPU after delta unions
            sum_tpu, sum_tpl = 0, 0
            for j in range(n):
                _, tpl, tpu = ruf_pc.pc_ranked_find(j)
                # print(tpl, tpu)
                sum_tpu += tpu
                sum_tpl += tpl
            # print(sum_tpu/n, sum_tpl/n)
            avg_tpl_pc.append(sum_tpl / n)
            avg_tpu_pc.append(sum_tpu / n)
            idx_pc.append(i)

    # Do the same thing for path splitting
    for i, pair in enumerate(comb):
        print(3, i)
        ruf_ps.union_by_rank(pair[0], pair[1])
        if ruf_ps.nr_blocks == 1:
            # Abort the queue once there is only one block left
            break
        if i % delta == 0:
            # Get average TPL and TPU after delta unions
            sum_tpu, sum_tpl = 0, 0
            for j in range(n):
                _, tpl, tpu = ruf_ps.ps_ranked_find(j)
                sum_tpu += tpu
                sum_tpl += tpl
            # print(sum_tpu/n, sum_tpl/n)
            avg_tpl_ps.append(sum_tpl / n)
            avg_tpu_ps.append(sum_tpu / n)
            idx_ps.append(i)

    # Do the same thing for path halving ph
    for i, pair in enumerate(comb):
        print(4, i)
        ruf_ph.union_by_rank(pair[0], pair[1])
        if ruf_ph.nr_blocks == 1:
            # Abort the queue once there is only one block left
            break
        if i % delta == 0:
            # Get average TPL and TPU after delta unions
            sum_tpu, sum_tpl = 0, 0
            for j in range(n):
                _, tpl, tpu = ruf_ph.ph_ranked_find(j)
                sum_tpu += tpu
                sum_tpl += tpl
            # print(sum_tpu/n, sum_tpl/n)

            avg_tpl_ph.append(sum_tpl / n)
            avg_tpu_ph.append(sum_tpu / n)
            idx_ph.append(i)

    fig, axs = plt.subplots(2, 2, figsize=(15, 8))

    # Subplot for no path compression
    axs[0, 0].plot(idx_nc, avg_tpl_nc, label='Total path length with no compression')
    axs[0, 0].plot(idx_nc, avg_tpu_nc, label='Total pointer updates with no compression')
    axs[0, 0].set_xlabel(f'Number of pairs processed with N = {delta}')
    axs[0, 0].set_ylabel('Average path length/pointer updates')
    axs[0, 0].legend()

    # Subplot for full path compression
    axs[0, 1].plot(idx_pc, avg_tpl_pc, label='Total path length with full compression')
    axs[0, 1].plot(idx_pc, avg_tpu_pc, label='Total pointer updates with full compression')
    axs[0, 1].set_xlabel(f'Number of pairs processed with N = {delta}')
    axs[0, 1].set_ylabel('Average path length/pointer updates')
    axs[0, 1].legend()

    # Subplot for path splitting
    axs[1, 0].plot(idx_ps, avg_tpl_ps, label='Total path length with path splitting')
    axs[1, 0].plot(idx_ps, avg_tpu_ps, label='Total pointer updates with path splitting')
    axs[1, 0].set_xlabel(f'Number of pairs processed with N = {delta}')
    axs[1, 0].set_ylabel('Average path length/pointer updates')
    axs[1, 0].legend()

    # Subplot for path halving
    axs[1, 1].plot(idx_ph, avg_tpl_ph, label='Total path length with path halving')
    axs[1, 1].plot(idx_ph, avg_tpu_ph, label='Total pointer updates with path halving')
    axs[1, 1].set_xlabel(f'Number of pairs processed with N = {delta}')
    axs[1, 1].set_ylabel('Average path length/pointer updates')
    axs[1, 1].legend()

    # Saving the figure
    # fig.tight_layout()
    fig.suptitle(
        f'{n} sample with ranked union and where the last pair processed at {idx_nc[-1]} with delta={delta}')
    plt.savefig(f'plots/rankedunion_examples_{n}_evaluated_{delta}.png')

    # plt.show()
