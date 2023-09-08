class PalindromeChecker:
    def __init__(self):
        self.stack = []
        self.queue = []

    def is_palindrome(self, input_str):
        input_str = ''.join([char for char in input_str if char.isalnum()])  # Remove non-alphanumeric characters
        input_str = input_str.lower()  # Convert to lowercase for case-insensitive comparison

        for char in input_str:
            self.stack.append(char)
            self.queue.append(char)

        while self.stack and self.queue:
            if self.stack.pop() != self.queue.pop(0):
                return False

        return True

# Test the palindrome checker
checker = PalindromeChecker()
print(checker.is_palindrome("(1+2)-3*[41+6]"))  # True
print(checker.is_palindrome("(1+2)-3*[41+6}"))  # False
print(checker.is_palindrome("(1+2)-3*[41+6"))   # False
print(checker.is_palindrome("(1+[2-3]*4{41+6})"))  # True
def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False

    return len(stack) == 0

# Test the expression balance checker
print(is_balanced("(1+2)-3*[41+6]"))  # True
print(is_balanced("(1+2)-3*[41+6}"))  # False
print(is_balanced("(1+2)-3*[41+6"))   # False
print(is_balanced("(1+[2-3]*4{41+6})"))  # True
class Car:
    def __init__(self, make, color, plate_number):
        self.make = make
        self.color = color
        self.plate_number = plate_number

class CarWash:
    def __init__(self):
        self.queue = []

    def enqueue(self, car):
        self.queue.append(car)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return None

# Example usage of the Car Wash program
car_wash = CarWash()
car_wash.enqueue(Car("Toyota", "Blue", 12345))
car_wash.enqueue(Car("Ford", "Red", 67890))

while not car_wash.isEmpty():
    car = car_wash.dequeue()
    if car:
        print(f"Washed car: {car.make}, {car.color}, Plate: {car.plate_number}")
def decode_message(message):
    stack = []
    result = []

    for char in message:
        if char.isalpha() or char.isspace():
            stack.append(char)
        elif char == '*':
            if stack:
                stack.pop()

    while stack:
        result.append(stack.pop())

    return ''.join(result[::-1])  # Reverse the result

# Test the message decoding function
decoded_message = decode_message("SIVLE ****** DAED TNSI ***")
print(decoded_message)  # Output: "ELVIS ISNT DEAD