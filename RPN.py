# 4 8 7 + 2 * 3 1 - * +
# 3 4 + 5 *
# 7 4 + 3 - 2 5 * /
# Operators: + - * / // % **
# Operands: integers, floats

# Infix: 2 + 3
# Prefix: + 2 3
# Postfix: 2 3 +

# Postfix:
# everytime I meet with an Operand I push on the stack
# everytime I meet with an Operator I pop twice from the stack
# and apply the operator and push the result on the stack

# when I have finished passing the expression there should be only one number
# in the stack and that should be the result of the postfix expression

# 4 8 7
# 8 + 7 = 15
# 4 15
# 4 15 2
# 15 * 2 = 30
# 4 30
# 4 30 3 1
# 3 - 1 = 2
# 4 30 2
# 30 * 2 = 60
# 4 + 60 = 64

class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


def operate(operand1, operand2, token):
    expr = str(operand1) + token + str(operand2)
    return eval(expr)


# reverse polish notation

def rpn(s):
    theStack = Stack()
    operators = ['+', '-', '*', '/', '//', '%', '**']
    tokens = s.split()
    for item in tokens:
        if item in operators:
            operand2 = theStack.pop()
            operand1 = theStack.pop()
            theStack.push(operate(operand1, operand2, item))
        else:
            theStack.push(item)
    return theStack.pop()


# postfix:
# 4 8 7 + 2 * 3 1 - * +

# infix:
# 4 + ((8 + 7) * 2) * (3 - 1))

def str_operate(operand1, operand2, token, last):
    # if you don't want the ending parenthesis
    if last:
        expr = str(operand1) + token + str(operand2)
    else:
        expr = "(" + str(operand1) + token + str(operand2) + ")"
    return expr


def postfix_to_infix(s):
    theStack = Stack()
    operators = ['+', '-', '*', '/', '//', '%', '**']
    tokens = s.split()
    idx = 0
    for item in tokens:
        if idx == len(tokens) - 1:
            operand2 = theStack.pop()
            operand1 = theStack.pop()
            theStack.push(str_operate(operand1, operand2, item, True))
        elif item in operators:
            operand2 = theStack.pop()
            operand1 = theStack.pop()
            theStack.push(str_operate(operand1, operand2, item, False))
        else:
            theStack.push(item)
        idx += 1
    return theStack.pop()


# 4 8 7 + 2 * 3 1 - * +
# 3 4 + 5 *
# 7 4 + 3 - 2 5 * /
# Operators: + - * / // % **
# Operands: integers, floats

# Prefix: + 2 3

def prefix(s):
    theStack = Stack()
    operators = ['+', '-', '*', '/', '//', '%', '**']
    tokens = s.split()
    for item in tokens[::-1]:
        if item in operators:
            operand2 = theStack.pop()
            operand1 = theStack.pop()
            theStack.push(operate(operand2, operand1, item))
        else:
            theStack.push(item)
    return theStack.pop()


def prefix_to_infix(s):
    theStack = Stack()
    operators = ['+', '-', '*', '/', '//', '%', '**']
    tokens = s.split()
    idx = len(tokens)
    for item in tokens[::-1]:
        if idx == 0:
            operand2 = theStack.pop()
            operand1 = theStack.pop()
            theStack.push(str_operate(operand2, operand1, item, True))
        elif item in operators:
            operand2 = theStack.pop()
            operand1 = theStack.pop()
            theStack.push(str_operate(operand2, operand1, item, False))
        else:
            theStack.push(item)
        idx -= 1
    return theStack.pop()


def operate(operand1, operand2, token):
    expr = str(operand1) + token + str(operand2)
    return int(eval(expr))


# Prefix: 2 + 3
def precedence(item):
    if item == "+" or item == "-":
        return 1
    elif item == "*" or item == "/" or item == "%" or item == "//":
        return 2
    elif item == "**":
        return 3
    else:
        return 0


def infix(s):
    operandStack = Stack()
    operatorStack = Stack()
    operators = ['+', '-', '*', '/', '//', '%', '**']

    tokens = s.split()
    for item in tokens:
        if item in operators:
            if operatorStack.is_empty():
                operatorStack.push(item)
            elif not operatorStack.is_empty():
                if precedence(item) >= precedence(operatorStack.peek()):
                    operatorStack.push(item)
                else:
                    while not operatorStack.is_empty():
                        op1 = operandStack.pop()
                        op2 = operandStack.pop()
                        operator1 = operatorStack.pop()
                        operandStack.push(operate(op2, op1, operator1))
                    operatorStack.push(item)
        elif item == '(':
            operatorStack.push(item)
        elif item == ')':
            while operatorStack.size() != 0 and operatorStack.peek() != '(':
                op1 = operandStack.pop()
                op2 = operandStack.pop()
                operator1 = operatorStack.pop()
                operandStack.push(operate(op1, op2, operator1))
            operatorStack.pop()
            # print(operatorStack.stack)
            # print(operandStack.stack)
        else:
            operandStack.push(item)
            # print(operatorStack.stack)
            # print(operandStack.stack)
    # print(operatorStack.stack)
    # print(operandStack.stack)
    while not operatorStack.is_empty():
        op1 = operandStack.pop()
        op2 = operandStack.pop()
        operator1 = operatorStack.pop()
        operandStack.push(operate(op2, op1, operator1))
    return operandStack.pop()


def infix_to_postfix(s):
    operatorStack = Stack()
    postfix = ""
    operators = ['+', '-', '*', '/', '//', '%', '**']
    tokens = s.split()
    for item in tokens:
        if item in operators:
            if operatorStack.is_empty():
                operatorStack.push(item)
            elif not operatorStack.is_empty():
                if precedence(item) >= precedence(operatorStack.peek()):
                    operatorStack.push(item)
                else:
                    while not operatorStack.is_empty() and precedence(item) < precedence(operatorStack.peek()):
                        operator1 = operatorStack.pop()
                        postfix += " " + operator1
                    operatorStack.push(item)
        elif item == '(':
            operatorStack.push(item)
        elif item == ')':
            while operatorStack.size() != 0 and operatorStack.peek() != '(':
                operator1 = operatorStack.pop()
                postfix += " " + operator1
            operatorStack.pop()

        else:
            postfix += " " + item
    while not operatorStack.is_empty():
        operator1 = operatorStack.pop()
        postfix += " " + operator1
    return postfix


def infix_to_prefix(s):
    operatorStack = Stack()
    postfix = ""
    operators = ['+', '-', '*', '/', '//', '%', '**']
    tokens = s.split()
    for item in tokens[::-1]:
        #print("item:",item)
        if item in operators:
            if operatorStack.is_empty():
                operatorStack.push(item)
                # print(postfix)
                # print(operatorStack.stack)
            elif not operatorStack.is_empty():
                if precedence(item) >= precedence(operatorStack.peek()):
                    operatorStack.push(item)
                    # print(postfix)
                    # print(operatorStack.stack)
                else:
                    while not operatorStack.is_empty() and precedence(item) <= precedence(operatorStack.peek()):
                        operator1 = operatorStack.pop()
                        postfix += " " + operator1
                        # print(postfix)
                        # print(operatorStack.stack)
                    operatorStack.push(item)
        elif item == ')':
            operatorStack.push(item)
            # print(postfix)
            # print(operatorStack.stack)
        elif item == '(':
            while operatorStack.peek() != ')':
                operator1 = operatorStack.pop()
                postfix += " " + operator1
                # print(postfix)
                # print(operatorStack.stack)
            operatorStack.pop()
        else:
            postfix += " " + item
            # print(postfix)
            # print(operatorStack.stack)
    while not operatorStack.is_empty():
        operator1 = operatorStack.pop()
        postfix += " " + operator1
    return postfix[::-1]


def main():
    in_file = open("rpn.txt", "r")
    i = 0
    for line in in_file:
        if i < 3:
            line = line.strip()
            value = rpn(line)
            print("postfix", line, " = ", value)
            value = postfix_to_infix(line)
            print("postfix to infix", line, " = ", value)
        elif i == 7:
            line = line.strip()
            value = infix(line)
            print("infix", line, " = ", value)
            value = infix_to_postfix(line)
            print("infix to postfix", line, " = ", value)
            value = infix_to_prefix(line)
            print("infix to prefix", line, " = ", value)
        else:
            line = line.strip()
            value = prefix(line)
            print("prefix", line, " = ", value)
            value = prefix_to_infix(line)
            print("prefix to infix", line, " = ", value)
        i += 1
    in_file.close()


main()
# 3 4 +
# 3 + 4
