class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = Stack()
        for op in operations:
            print(stack.items)
            if op == "+":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.double_push([op1, op2, op1 + op2])
            elif op == "D":
                op1 = stack.pop()
                stack.double_push([op1, op1 * 2])
            elif op == "C":
                stack.pop()
            else:
                stack.push(int(op))
        return stack.total()
class Stack:
    def __init__(self):
        self.items = []
    def push(self, other):
        self.items.append(other)
    def double_push(self, other):
        self.items += other
    def pop(self):
        return self.items.pop()
    def total(self):
        return sum(self.items)