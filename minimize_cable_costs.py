import heapq
import random


def minimize_cable_costs(cables):
    heapq.heapify(cables)  # convert list to heap

    while len(cables) > 1:
        smallest1 = heapq.heappop(cables)  # pop smallest cable
        smallest2 = heapq.heappop(cables)
        length_sum = smallest1 + smallest2  # add cable lengths
        heapq.heappush(cables, length_sum)  # push new connected cable

    return cables[0]


if __name__ == '__main__':
    # makes 10 random cable lengths
    cables = [random.randint(1, 50) for _ in range(10)]
    print("Original cables:", cables)
    result = minimize_cable_costs(cables)
    print("Minimized total cost:", result)
