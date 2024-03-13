import random
def main():
    def binary_search(lst, target):
        first = 0
        last = len(lst) - 1
        while first <= last:
            midpoint = (first + last) // 2
            if lst[midpoint] == target:
                return midpoint
            elif lst[midpoint] < target:
                first = midpoint + 1
            else:
                last = midpoint - 1
        return None

    def guess_number():
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = random.choice(numbers)
        print("You're given a list from 1 to 10. What number am I thinking of?")

        while True:
            try:
                guess_input = int(input("Enter your guess: "))
                if guess_input < 1 or guess_input > 10:
                    print("Please enter a number between 1 and 10.")
                    continue
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if guess_input == target:
                print("You're correct!")
                break
            elif guess_input > target:
                print("Too high.")
            else:
                print("Too low.")

    guess_number()
main()