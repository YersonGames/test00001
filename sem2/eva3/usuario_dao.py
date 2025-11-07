from database import Database
from usuario import Usuario

class UsuarioDAO:
    def __init__(self):
        self.database = Database()
        self._create_table()

    def _create_table(self):
        with self.database.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS usuario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    contrasena TEXT NOT NULL,
                    sal TEXT NOT NULL
                )
            ''')

    def insertar(self, usuario):
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuario (nombre, contrasena,sal) VALUES (?, ?, ?)', 
                           (usuario.get_nombre(), usuario.get_contrasenahash(),usuario.get_sal()))
            conn.commit()

    def login_username(self,nombre):
        with self.database.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT contrasena, sal, id FROM usuario WHERE nombre = ?', 
                           (nombre,))
            select = cursor.fetchone()
            if not select:
                print("El usuario o contraseña es incorrecta.")
            else:
                return select