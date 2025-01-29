note["username"]=input("Имя пользователя:")
note["title"]=input("Заголовок заметки:")
note["content"]= input("описание заметки:")
note["status"]= input("статус заметки:")
note["created_date"]=input("дата создания заметки в формате 'день-месяц-год':")
note["issue_date"]= input("Дата истечения заметки в формате 'день-месяц-год':")
note["titles"]=[]
for i in range(3):
    title=input(f"Введите заголовок заметки {i+1}:")
    note["titles"].append(title)
for key, value in note.items():
    print(f"{key.capitalize()}:{value}")
