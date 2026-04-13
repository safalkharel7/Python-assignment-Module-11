class Publication:
    def __init__(self, name):
        self.name=name

    def print_information(self):
        print(f"Name: {self.name}")
class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}\nPage Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.editor}")

Item1= Magazine("Donald Duck","Aki Hyyppä")
Item2= Book("Compartment No. 6.","Rosa Liksom", 192)
print()
Item1.print_information()
print()
Item2.print_information()