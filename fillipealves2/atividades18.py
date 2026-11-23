ARQUIVO = "tarefas.txt"

while True:
  print("\n1. Adicionar tarefa | 2. Listar tarefas | 3. Sair")
  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    tarefa = input("Descrição da tarefa: ")
    with open(ARQUIVO, "a", encoding="utf-8") as f:
      f.write(tarefa + "\n")
    print("Tarefa salva!")

  elif opcao == "2":
    try:
      with open(ARQUIVO, "r", encoding="utf-8") as f:
        tarefas = f.readlines()
      if not tarefas:
        print("Nenhuma tarefa cadastrada.")
      for idx, t in enumerate(tarefas, 1):
        print(f"{idx}. {t.strip()}")
    except FileNotFoundError:
      print("Nenhuma tarefa encontrada ainda.")

  elif opcao == "3":
    print("Encerrando...")
    break
  else:
    print("Opção inválida.")