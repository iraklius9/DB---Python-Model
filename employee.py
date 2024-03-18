from db import c


class Employee(object):
    def __init__(self, name, surname, age, id=None):     # noqa
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def get(cls, employee_id):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (employee_id,))
        data = result.fetchone()
        if data:
            return cls(**data)
        else:
            return None

    @classmethod
    def get_list(cls, **kwargs):
        query = f"SELECT * FROM employee"
        filter = " AND ".join([f"{key} = ?" for key in kwargs])  # noqa
        if filter:
            query += f" WHERE {filter}"

        result = c.execute(query, list(kwargs.values()))
        return [cls(*row) for row in result.fetchall()]

    def delete(self):
        c.execute("DELETE FROM employee WHERE id = ?", (self.id,))

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __repr__(self):
        return f"<Employee {self.name} {self.surname}, Age: {self.age}>"

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))

    def create(self):
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self
