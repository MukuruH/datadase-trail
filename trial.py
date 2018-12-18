import psycopg2
import psycopg2.extras
import os

class Databaseconnect:
    def __init__(self):
        connection = psycopg2.connect(dbname='sim_assgn', user='hamza',
                                     password='123456789', host='localhost', port='5432')

        connection.autocommit=True
        self.cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        

        create_human_table=""" CREATE TABLE IF NOT EXISTS human (id SERIAL PRIMARY KEY,
                                name VARCHAR(25) NOT NULL, address CHAR(7) NULL, age INT,
                                single BOOLEAN NULL);"""
        
        self.cursor.execute(create_human_table)

        create_simcard_table=""" CREATE TABLE IF NOT EXISTS simcard (id SERIAL PRIMARY KEY, name VARCHAR(25) NOT NULL,
                                phone_number INT NOT NULL, serial NUMERIC,
                                service_proviider VARCHAR(25) NOT NULL, is_active BOOLEAN );"""
        
        self.cursor.execute(create_simcard_table)

    
    def get_human_table(self):
        command="""
        SELECT * FROM human;
        """
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        return rows

    def add_to_human(self, name, address, age, single):
        command="""
        INSERT INTO human(name, address, age, single)
        VALUES('{name}', '{address}', '{age}', '{single}');
            """.format(name=name, address=address,age=age,single=single)

        self.cursor.execute(command)
        rowcount = self.cursor.rowcount
        return rowcount

    def update_human(self, name, address, age, single):
        command="""
        UPDATE human
        SET name='{name}', address='{address}', age='{age}', single='{single}'
        WHERE id={id}
            """.format(name=name, address=address,age=age,single=single,id=id)

        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        return rows

    def delete_from_human(self, id):
        command="""
        DELETE FROM human WHERE id='{id}';
        """.format(id=id)

        self.cursor.execute(command)
        rowcount = self.cursor.rowcount
        return rowcount

    def get_simcard_table(self):
        command="""
        SELECT * FROM simcard;
        """
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        return rows

    def add_to_simcard(self, name, phone_number, serial, service_proviider, is_active):
        command="""
        INSERT INTO simcard(name, phone_number, serial, service_proviider, is_active)
        VALUES('{name}', '{phone_number}', '{serial}', '{service_provider}','{is_active}');
            """.format(name=name, phone_number=phone_number,serial=serial,service_proviider=service_proviider,is_active=is_active)

        self.cursor.execute(command)
        rowcount = self.cursor.rowcount
        return rowcount

    def update_simcard(self, name, phone_number, serial, service_proviider, is_active):
        command="""
        UPDATE simcard
        SET name='{name}', phone_number='{phone_number}',serial='{serial}',service_proviider='{service_proviider}',is_active='{is_active}'
        WHERE id={id}
            """.format(name=name, address=address,age=age,single=single,id=id)

        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        return rows

    def delete_from_simcard(self, id):
        command="""
        DELETE FROM simcard WHERE id='{id}';
        """.format(id=id)

        self.cursor.execute(command)
        rowcount = self.cursor.rowcount
        return rowcount


if __name__ == "__main__":
    db_run= Databaseconnect()
    #db_run.add_to_human('hamza','here56',57,'yes')
    db_run.delete_from_human(2)
    print(db_run.get_human_table())
    
  
   