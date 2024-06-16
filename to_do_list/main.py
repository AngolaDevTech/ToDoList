import sqlite3
from db_operations import add_task, view_tasks, complete_task, delete_task

def show_menu():
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Excluir Tarefa")
    print("5. Sair")

def main():
    while True:
        show_menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            title = input("Título da tarefa: ")
            description = input("Descrição da tarefa (opcional): ")
            add_task(title, description)
            print("Tarefa adicionada com sucesso!\n")

        elif choice == '2':
            tasks = view_tasks()
            for task in tasks:
                status = "Concluída" if task[3] else "Pendente"
                print(f"{task[0]}. {task[1]} - {task[2]} [{status}]")
            print()

        elif choice == '3':
            task_id = int(input("ID da tarefa a ser marcada como concluída: "))
            complete_task(task_id)
            print("Tarefa marcada como concluída!\n")

        elif choice == '4':
            task_id = int(input("ID da tarefa a ser excluída: "))
            delete_task(task_id)
            print("Tarefa excluída!\n")

        elif choice == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
