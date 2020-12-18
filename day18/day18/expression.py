class Expression:

    expression_string = ""
    output = []
    tokens = []
    result = 0

    def __init__(self, expression_string):
        self.expression_string = expression_string.strip()
        self.output = []
        self.result = 0

    def tokenize(self):

        self.tokens = []

        # Need to walk it by index
        i = 0
        while i < len(self.expression_string):
            
            if self.expression_string[i] in "0123456789":
                self.tokens.append(int(self.expression_string[i]))
            elif self.expression_string[i] in "()+*":
                self.tokens.append(self.expression_string[i])

            i+=1

    def parse(self):

        op_stack = []

        self.tokenize()

        for token in self.tokens:
            if type(token) is int:
                self.output.append(token)

            elif token in "+*":
                if not op_stack:
                    op_stack.append(token)
                else:
                    while op_stack:
                        operator = op_stack.pop()
                        if operator == "(":
                            op_stack.append(operator)
                            break
                        else:
                            self.output.append(operator)
                    op_stack.append(token)
            
            elif token == "(":
                op_stack.append(token)

            elif token == ")":
                operator = op_stack.pop()
                while operator != "(":
                    self.output.append(operator)
                    operator = op_stack.pop()

        while op_stack:
            self.output.append(op_stack.pop())

    def parse_prec(self):

        op_stack = []

        self.tokenize()

        for token in self.tokens:
            if type(token) is int:
                self.output.append(token)

            elif token in "+*":
                if not op_stack:
                    op_stack.append(token)
                else:
                    while op_stack:
                        operator = op_stack.pop() 
                        if operator == "(":
                            op_stack.append(operator)
                            break
                        elif token == "*" or (token == "+" and operator=="+"):
                            self.output.append(operator)
                        else:
                            op_stack.append(operator)
                            break
                    op_stack.append(token)
            
            elif token == "(":
                op_stack.append(token)

            elif token == ")":
                operator = op_stack.pop()
                while operator != "(":
                    self.output.append(operator)
                    operator = op_stack.pop()

        while op_stack:
            self.output.append(op_stack.pop())


    def evaluate(self):
        operand_stack = []
        
        for token in self.output:
            if type(token) is int:
                operand_stack.append(token)
            elif token == "+":
                op1 = operand_stack.pop()
                op2 = operand_stack.pop()
                operand_stack.append(op1 + op2)
            elif token == "*":
                op1 = operand_stack.pop()
                op2 = operand_stack.pop()
                operand_stack.append(op1 * op2)

        return operand_stack[0]