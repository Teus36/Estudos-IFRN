from database import get_connection 

class Emprestimo:
    def __init__(self, book_id, user_id):
        self.book_id = book_id
        self.user_id = user_id

    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO tb_emprestimos(emp_book_id, emp_user_id) values(?,?)", (self.book_id, self.user_id))
        conn.commit()
        conn.close()
        return True

    @classmethod
    def all(cls):
        conn = get_connection()
        emprestimos = conn.execute("SELECT * FROM tb_emprestimos").fetchall()
        return emprestimos