class Solution:
    def calPoints(self, operations: List[str]) -> int:
        items = []
        for op in operations:
            if op == "+":
                items.append(items[-1] + items[-2])
            elif op == "D":
                items.append(items[-1] * 2)
            elif op == "C":
                items.pop()
            else:
                items.append(int(op))
        return sum(items)
