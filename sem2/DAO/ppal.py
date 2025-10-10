from persona import Persona
from persona_dao import PersonaDAO

# Crear instancia de PersonaDAO
persona_dao = PersonaDAO()

def mostrar_menu():
    print("1- Crear persona")
    print("2- Listar personas")
    print("3- Actualizar persona")
    print("4- Eliminar persona")
    print("0- Salir")

def main():
    salir = 0
    while salir == 0:
        mostrar_menu()
        opcion = input("Opcion: ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                edad = input("Edad: ")
                nueva_persona = Persona(None, nombre, edad)
                persona_dao.insertar(nueva_persona)
                print(f'Persona insertada: {nueva_persona}')
            elif opcion == "2":
                personas = persona_dao.seleccionar_todos()
                print('Lista de personas:')
                for persona in personas:
                    print(f"ID: {persona[0]} Nombre: {persona[1]} Edad: {persona[2]}")
            elif opcion == "3":
                try:
                    nombre = input("Nombre de la persona a actualizar: ").strip()

                    for p in persona_dao.seleccionar_todos():
                        actnombre = str(p[1])
                        if nombre.lower() in actnombre.lower():
                            print(f"Persona a actualizar: {p[1]}")
                            nnombre = input("Nombre nuevo: ")
                            nedad = int(input(f"Edad nueva: "))
                            personas = [Persona(p[0],p[1],p[2])]
                            if personas:
                                #persona_actualizar = personas[0]
                                persona_actualizar = Persona(p[0],nnombre,nedad)
                                persona_dao.actualizar(persona_actualizar)
                                print(f'Persona actualizada: {p[1]}, Edad: {p[2]}')
                except Exception as error:
                    print("Error:",error)
            elif opcion == "4":
                try:
                    nombre = input("Nombre de la persona a eliminar: ").strip()

                    for p in persona_dao.seleccionar_todos():
                        actnombre = str(p[1])
                        if nombre.lower() in actnombre.lower():
                            personas = [Persona(p[0],p[1],p[2])]
                            if personas:
                                persona_dao.eliminar(p[0])
                                print(f'Persona eliminada: {p[1]}')
                except Exception as error:
                    print("Error:",error)
            elif opcion == "0":
                salir = 1


                
        except Exception as error:
            print(error)

main()