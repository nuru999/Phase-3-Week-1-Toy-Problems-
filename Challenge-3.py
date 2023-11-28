def solve(s):
    def calculate_value(substring):
        return sum(ord(c) - ord('a') + 1 for c in substring)
    
    vowels = set("aeiou")
    current_consonant = ''
    consonant_values = []
    
    for char in s:
        if char not in vowels:
            current_consonant += char
        else:
            if current_consonant:
                consonant_values.append(calculate_value(current_consonant))
                current_consonant = ''
    
    if current_consonant:
        consonant_values.append(calculate_value(current_consonant))
    
    return max(consonant_values) if consonant_values else 0