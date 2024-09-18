def are_parentheses_balanced(chars):
    stack = []
    matching_parentheses = {')': '(', ']': '[', '}': '{'}
    
    for char in chars:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if matching_parentheses[char] != top:
                return False
    
    return not stack

# Test cases
print(are_parentheses_balanced(list(":-)")))  # False
print(are_parentheses_balanced(list("())( ")))  # False
print(are_parentheses_balanced(list("{[()]}")))  # True