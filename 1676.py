def solution():
    company_count = int(input())
    sold_count = []
    for i in range(company_count):
        sold_count.append(int(input()))

    company_rank = rank_company(sold_count)
    for i in company_rank:
        print(i)


def rank_company(sold_count):
    company_rank = sold_count[:]
    sold_count_set = list(set(sold_count))
    sold_count_set.sort(reverse=True)

    rankcount = 0
    for i in range(len(sold_count_set)):
        samenumber = 0
        for j in range(len(sold_count)):
            if sold_count_set[i] == sold_count[j]:
                company_rank[j] = rankcount + 1
                samenumber += 1
        rankcount += samenumber

    return company_rank


solution()
