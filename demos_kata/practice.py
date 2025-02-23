def decode(message_file):
    lines_to_extract = ['I', 'love', 'computers']  # Replace with the words you want

    with open(message_file, 'r') as file:
        lines = file.readlines()

    decoded_words = []

    for line in lines:
        words = line.split()
        if words[1] in lines_to_extract:
            decoded_words.append(words[1])
            # reverse the list so we can get i love computers instead of love computers i 
            decoded_words = list(reversed(decoded_words))
            

    decoded_message = ' '.join(decoded_words)

    return decoded_message

# Example usage
decoded_message = decode('coding_qual_input.txt') 

print(decoded_message)
