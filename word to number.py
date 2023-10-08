def words_to_digits(input_str):
    word_to_digit = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "double": "",
        "triple": ""
    }

    words = input_str.split()
    result = ""
    i = 0

    while i < len(words):
        if words[i] in word_to_digit:
            count = 0
            current_word = words[i]
            while i < len(words) and words[i] == current_word:
                count += 1
                i += 1
            if current_word == "double":
                result += word_to_digit[current_word] * 2 * count
            elif current_word == "triple":
                result += word_to_digit[current_word] * 3 * count
            else:
                result += word_to_digit[current_word] * count

    return result

# Example usage:
input_str1 = "two one nine six eight one six four six zero"
output1 = words_to_digits(input_str1)
print(output1)  # Output: "2196816460"

input_str2 = "five one zero two four eight zero double three two"
output2 = words_to_digits(input_str2)
print(output2)
