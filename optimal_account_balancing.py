"""
A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.
"""
class Solution:
    def minTransfers(self, transactions):
        # Create graph with transactions
        #   { x: { y: z } }
        # Traverse graph and reconcilate any debts that conflict
        graph = {}
        for transaction in transactions:
            if transaction[0] in graph:
                if transaction[1] in graph[transaction[0]]:
                    graph[transaction[0]][transaction[1]] = transaction[2]
            else:
                graph[transaction[0]] = { transaction[1]: transaction[2] }

        return graph
        # for transaction in transactions:


solution = Solution()
print(solution.minTransfers([[0, 1, 10], [2, 0, 5]]))
