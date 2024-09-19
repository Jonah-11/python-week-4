import json
import difflib

# Load dictionary data from a JSON file
def load_dictionary(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to get the definition of a word
def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        # Suggest closest matches if the word is not found
        closest_matches = difflib.get_close_matches(word, dictionary.keys())
        if closest_matches:
            suggestion = closest_matches[0]
            return f"Word not found. Did you mean '{suggestion}'? Definition: {dictionary[suggestion]}"
        else:
            return "Word not found and no suggestions available."

# Main program
def main():
    dictionary = load_dictionary('./Dictionary.json')
    
    while True:
        word = input("Enter a word and i'll define it(type 'exit' to exit): ")
        if word.lower() == 'exit':
            break
        definition = get_definition(word, dictionary)
        print(definition)

if __name__ == "__main__":
    main()
