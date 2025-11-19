from database import Database

class RegistroDAO:
    def __init__(self):
        self.database = Database()
        self._create_table()

    def _create_table(self):
        with self.database.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS registro (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_usuario INTEGER NOT NULL,
                    valor_dolar REAL NOT NULL,
                    fecha DATE NOT NULL
                )
            ''')

    def registrar(self,id_usuario,fecha,usd):
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO registro (id_usuario, fecha,valor_dolar) VALUES (?, ?, ?)', 
                           (id_usuario,fecha,usd))
            conn.commit()

    def consultar(self):
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            SELECT r.id, u.nombre, r.valor_dolar,r.fecha
                            FROM registro as r
                            LEFT JOIN usuario as u ON r.id_usuario = u.id''')
            select = cursor.fetchall()
            if not select:
                print("No hay registros.")
            else:
                return select
