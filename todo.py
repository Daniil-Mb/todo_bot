HELP = """
HELP - помощь
add  - добавить
show  - показать
done   - убрать
exit    - выкл
"""

todo = {} 
print("Введите команду или HELP, для вывода доступных команд")

while True:
  userUnswer = input()

  if userUnswer == "add":
    print("Работает ")
  elif userUnswer == "help":
    print(HELP) 
  elif userUnswer == "show":
    print("Работает ") 
  elif userUnswer == "exit":
    break
  elif userUnswer == "done":
    print("Работает ") 

