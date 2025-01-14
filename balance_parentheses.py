# Check if the string contains balanced parenthesis or not

def balance_parentheses(input_string):
    open_brackets = '{[('  # define all open brackets
    closed_brackets = '}])'  # define all closed brackets
    bracket_stack = []  # Initialize an empty list to store brackets

    for val in input_string:
        if val in open_brackets:
            bracket_stack.append(val)  # Append open bracket to stack
        else:
            if bracket_stack:  # Check if stack is not empty
                elem = bracket_stack[-1]  # Get the last element of the stack
                if (elem == "{" and val == "}") or (elem == "[" and val == "]") or (elem == "(" and val == ")"):
                    bracket_stack.pop()  # If last element matches the closed bracket, pop it
                else:
                    return "Not balanced"  # If last element does not match closed bracket, return "Not balanced"
            else:
                return "Not balanced"  # If stack is empty, return "Not balanced"

    if bracket_stack:  # Check if there are any remaining elements in stack
        return "Not balanced"  # If yes, return "Not balanced"
    return "Balanced"  # If not, return "Balanced"

print(balance_parentheses("[{}{}]"))  # Balanced
print(balance_parentheses("[{}{}(]"))  # Not balanced
