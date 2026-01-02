def isPalindrome(self, s: str) -> bool:
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    l = 0
    r = len(cleaned) - 1

    for _ in range(len(cleaned) - 1):
        if cleaned[l] == cleaned[r]:
            l += 1
            r -= 1
        else:
            return False
    return True   
