"""
Single Responsibility Principle (SPR)
Definition: A class should have only one reason to change, meaning that a class should have only one job or responsibility.
"""

#bad design
class Report:
    def generate(self):
        return "Report Data"

    def save_to_file(self, data):
        with open('report.txt', 'w') as f:
            f.write(data)
#good design

class Report:
    def generate(self):
        return "Report Data"

class ReportSaver:
    def save_to_file(self, data):
        with open('report.txt', 'w') as f:
            f.write(data)
