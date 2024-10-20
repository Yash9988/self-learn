"""
1106. Parsing A Boolean Expression [HARD]

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

    - 't' that evaluates to true.
    - 'f' that evaluates to false.
    - '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
    - '&(subExpr_1, subExpr_2, ..., subExpr_n)' that evaluates to the logical AND of the inner expressions subExpr_1,
        subExpr_2, ..., subExpr_n where n >= 1.
    - '|(subExpr_1, subExpr_2, ..., subExpr_n)' that evaluates to the logical OR of the inner expressions subExpr_1,
        subExpr_2, ..., subExpr_n where n >= 1.

Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.


Example 1:

Input: expression = "&(|(f))"
Output: false

Explanation:
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.


Example 2:

Input: expression = "|(f,f,f,t)"
Output: true

Explanation: The evaluation of (false OR false OR false OR true) is true.


Example 3:

Input: expression = "!(&(f,t))"
Output: true

Explanation:
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.


Constraints:

    -> 1 <= expression.length <= 2 * 104
    -> expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.


Concepts: Stack
"""


# My Solution
def parseBoolExpr(expression: str) -> bool:
    stack = []                                                  # Initialise a list/stack
    for shape in expression:                                    # Iterate through each "shape" in the expression
        if shape in '(|!&':                                     # Check if the shape is any operator or '('
            stack.append(shape)                                 # Append the shape directly into the stack
        elif shape == ',':                                      # Check if the shape is a ','
            continue                                            # Skip to the next iteration
        elif shape in 'tf':                                     # Check if the shape is a boolean expression
            stack.append(True if shape == 't' else False)       # Append the boolean into the stack
        else:                                                   # In the case where the shape is ')'
            temp = []                                           # Create another list to store all booleans
            while True:                                         # Iterate indefinitely
                x = stack.pop()                                 # Pop the last element from the stack
                if x == '(':                                    # Check if the shape is '('
                    break                                       # Break out of the loop
                temp.append(x)                                  # Append the element into the new list, otherwise

            x = stack.pop()                                     # Pop the last element from the stack (operator)
            stack.append(all(temp) if x == '&' else
                         (any(temp) if x == '|' else
                          not temp[0]))                         # Perform the corresponding operation on the booleans

    return stack[-1]                                            # Return the resulting boolean in the stack


# "Hacky" Solution
def parseBoolExpr_alt(S, t=True, f=False):
    return eval(S.replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))
