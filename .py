# Sample Python Code for SonarQube Analysis
 
class Calculator:
    def __init__(self):
        self.result = 0
 
    def add(self, num):
        """Add a number to the result."""
        self.result += num
 
    def subtract(self, num):
        """Subtract a number from the result."""
        self.result -= num
 
    def multiply(self, num):
        """Multiply the result by a number."""
        self.result *= num
 
    def divide(self, num):
        """Divide the result by a number."""
        if num != 0:
            self.result /= num
        else:
            print("Cannot divide by zero.")
 
    def get_result(self):
        """Get the current result."""
        return self.result
 
 
# Example Usage
calculator = Calculator()
calculator.add(5)
calculator.subtract(3)
calculator.multiply(4)
calculator.divide(2)
 
print("Result:", calculator.get_result())
