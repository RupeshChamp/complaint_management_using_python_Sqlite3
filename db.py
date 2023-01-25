import sqlite3


class ComplaintRegisterDatabase:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS complaintRegister(
        id Integer Primary Key,
        name text,
        age text,
        email text,
        gender text,
        contact text,
        address text,
        complaint text
        )
        """

        self.cur.execute(sql)
        self.con.commit()

    # Insert Function

    def insert(self, name, age, email, gender, contact, address, complaint):
        self.cur.execute("insert into complaintRegister values (NULL,?,?,?,?,?,?,?)",
                         (name, age, email, gender, contact, address, complaint))
        self.con.commit()

    def fetch(self):
        self.cur.execute("Select * from complaintRegister")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    def remove(self, id):
        self.cur.execute("delete from complaintRegister where id=?", (id,))
        self.con.commit()

    def update(self, id, name, age, email, gender, contact, address, complaint):
        self.cur.execute(
            "update complaintRegister set name=?,age=?,email=?,gender=?,contact=?,address=?,complaint=? where id=?",
            (name, age, email, gender, contact, address, complaint, id))
        self.con.commit()
