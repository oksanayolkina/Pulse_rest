class Book:

    def __init__(self, title=None, author=None, id=None):
        self.title = title
        self.author = author
        self.id = id

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def get_dict_without_id(self):
        return {"title": self.title, "author": self.author}

    def get_dict_with_id(self):
        return {"id": self.id, "title": self.title, "author": self.author}

class Role:

    def __init__(self, id=None, name=None, type=None, level=None, book=None):
        self.name = name
        self.type = type
        self.id = id
        self.level = level
        self.book = book

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def get_dict_without_id(self):
        return {"name": self.name, "type": self.type, "level": self.level, "book": self.book}

    def get_dict_with_id(self):
        return {"id": self.id, "name": self.name, "type": self.type, "level": self.level, "book": self.book}


if __name__ == "__main__":
    b = Book()
    print(b.title)

    c = Role()
    print(c.name)