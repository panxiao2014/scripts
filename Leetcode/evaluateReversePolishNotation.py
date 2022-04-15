#Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
#Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
#Note:
#
#Division between two integers should truncate toward zero.
#The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
#
#Example 1:
#
#Input: ["2", "1", "+", "3", "*"]
#Output: 9
#Explanation: ((2 + 1) * 3) = 9
#Example 2:
#
#Input: ["4", "13", "5", "/", "+"]
#Output: 6
#Explanation: (4 + (13 / 5)) = 6
#Example 3:
#
#Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#Output: 22
#Explanation: 
#  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#= ((10 * (6 / (12 * -11))) + 17) + 5
#= ((10 * (6 / -132)) + 17) + 5
#= ((10 * 0) + 17) + 5
#= (0 + 17) + 5
#= 17 + 5
#= 22


class Solution:
    def evalRPN(self, tokens):
        def isOperator(i):
          if(i=='+' or i=='-' or i=='*' or i=='/'):
            return True
          else:
            return False
          
        def compute(a, b, op):
          if(op=='+'):
            return a+b
          elif(op=='-'):
            return a-b
          elif(op=='*'):
            return a*b
          elif(op=='/'):
            return int(a/b)
          
          
        strLen = len(tokens)  
        opStack = []
        result = 0
        
        if(strLen == 1):
          return tokens[0]
        
        for i in range(0, strLen):
          if(isOperator(tokens[i]) == False):
            opStack.append(int(tokens[i]))
          else:
            b = opStack.pop()
            a = opStack.pop()
            result = compute(a, b, tokens[i])
            opStack.append(result)
            
        return result


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

solution = Solution()
print(solution.evalRPN(tokens))
