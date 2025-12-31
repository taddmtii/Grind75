def isValid(self, s: str) -> bool:
    stack = []
    closing_brackets = {")": "(", "]": "[", "}": "{"}
     
    for symbol in s:
       if symbol in closing_brackets.values():
           stack.append(symbol)
       elif symbol in closing_brackets:
           if stack and stack[-1] == closing_brackets[symbol]:
               stack.pop()
           else:
               return False
    return stack == []
