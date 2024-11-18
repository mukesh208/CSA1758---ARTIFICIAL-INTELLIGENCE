from itertools import permutations

def solve_cryptarithmetic(words, result):
    unique_chars = set("".join(words) + result)
    
    if len(unique_chars) > 10:
        print("No solution: More than 10 unique characters.")
        return
    
    for perm in permutations(range(10), len(unique_chars)):
        char_to_digit = dict(zip(unique_chars, perm))
        
        if any(char_to_digit[word[0]] == 0 for word in words + [result]):
            continue
        
        words_sum = sum(int("".join(str(char_to_digit[c]) for c in word)) for word in words)
        result_value = int("".join(str(char_to_digit[c]) for c in result))
        
        if words_sum == result_value:
            print("Solution Found!")
            print("Mapping:", char_to_digit)
            print(f"{' + '.join(words)} = {result}")
            return
    
    print("No solution exists.")

if __name__ == "__main__":
    print("Enter the cryptarithmetic puzzle in the form:")
    print("Words (space-separated) followed by the result word.")
    print("Example: SEND MORE MONEY")
    
    inputs = input("Enter puzzle: ").split()
    words = inputs[:-1]
    result = inputs[-1]
    
    solve_cryptarithmetic(words, result)
