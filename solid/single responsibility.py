'''SOLID Principles: Simplified Explanation with Example
The SOLID principles are five design principles for writing maintainable and scalable object-oriented software. They make the code easier to understand, extend, and refactor.'''

'''Single Responsibility Principle (SRP)
"A class should have only one reason to change."

Meaning: Each class should focus on one task or functionality.
Why: Reduces complexity, improves readability, and makes maintenance easier.'''

# Bad Example
class Report:
    def generate_report(self):
# FileSaver class handles file savin
        print("Generating Report")
    
    def save_to_file(self):
        print("Saving Report to File")

# Here, the Report class handles both report generation and file saving, violating SRP.

# Good Example (SRP Applied):

class ReportGeneration:
    def generate_report(self):
        print("Generating Report")

class FileSaver:
    def save_to_file(self, report):
        print("Saving Report to File")

# ReportGeneration class handles report generation.
# FileSaver class handles file saving.