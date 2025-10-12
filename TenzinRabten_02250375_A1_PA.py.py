def is_perfect(n):
    """Check if a number is perfect."""
    return n == sum(i for i in range(1, n) if n % i == 0)

def perfect_number_sum(start, end):
    """Calculate the sum of perfect numbers in a given range."""
    try:
        start, end = int(start), int(end)
        if start > end or start < 1:
            raise ValueError
        return sum(n for n in range(start, end + 1) if is_perfect(n))
    except ValueError:
        return "Invalid range. Please enter positive integers with start ≤ end."

def convert_weight(value, direction):
    """Convert weight between kilograms and pounds."""
    try:
        value = float(value)
        if direction.upper() == 'K':
            return round(value * 2.205, 2)
        elif direction.upper() == 'P':
            return round(value / 2.205, 2)
        else:
            return "Invalid direction. Use 'K' or 'P'."
    except ValueError:
        return "Invalid weight value."

def count_vowels(text):
    """Count vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def average_and_range(numbers):
    """Calculate average and range of a list of numbers."""
    try:
        nums = [float(n) for n in numbers]
        avg = sum(nums) / len(nums)
        rng = max(nums) - min(nums)
        return f"Average: {round(avg, 2)}, Range: {round(rng, 2)}"
    except ValueError:
        return "Invalid input. Please enter numeric values."

def reverse_and_word_count(text):
    """Reverse a string and count words."""
    reversed_text = text[::-1]
    word_count = len(text.strip().split())
    return f"Reversed: {reversed_text}\nWord count: {word_count}"

def count_specific_words():
    """Count occurrences of specific words in a text file."""
    url = "https://gist.githubusercontent.com/konrados/a1289ade329ac6f4598ebf5ee3dbcb3c/raw"
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8').lower()
        targets = ["is", "are", "has", "have"]
        counts = {word: content.split().count(word) for word in targets}
        return counts
    except Exception as e:
        return f"Error fetching file: {e}"

def main():
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate sum of perfect numbers")
        print("2. Convert weight units")
        print("3. Count vowels in string")
        print("4. Find average and range of numbers")
        print("5. Reverse string and count words")
        print("6. Count specific words in text file")
        print("0. Exit program")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            start = input("Enter start of range: ")
            end = input("Enter end of range: ")
            print("Sum of perfect numbers:", perfect_number_sum(start, end))

        elif choice == '2':
            value = input("Enter weight value: ")
            direction = input("Convert from (K for kg to lb, P for lb to kg): ")
            print("Converted weight:", convert_weight(value, direction))

        elif choice == '3':
            text = input("Enter a string: ")
            print("Number of vowels:", count_vowels(text))

        elif choice == '4':
            try:
                count = int(input("How many numbers will you enter? "))
                numbers = [input(f"Enter number {i+1}: ") for i in range(count)]
                print(average_and_range(numbers))
            except ValueError:
                print("Invalid count. Please enter an integer.")

        elif choice == '5':
            text = input("Enter a string: ")
            print(reverse_and_word_count(text))

        elif choice == '6':
            result = count_specific_words()
            for word, count in result.items():
                print(f"{word}: {count}")

        elif choice == '0':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 0 to 6.")

        again = input("Would you like to try another function? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for using the program!")
            break

if __name__ == "__main__":
    main()