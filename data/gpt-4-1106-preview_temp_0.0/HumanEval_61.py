def correct_bracketing(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket == '(':  # If it's an opening bracket, push to stack
            stack.append(bracket)
        elif bracket == ')':  # If it's a closing bracket
            if not stack or stack[-1] != '(':  # Check for corresponding opening
                return False
            stack.pop()  # Pop the opening bracket
    return not stack  # If stack is empty, all brackets are correctly closed
