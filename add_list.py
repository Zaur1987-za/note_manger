username=input("Имя пользователя:")
title=input("Заголовок заметки:")
content= input("описание заметки:")
status= input("статус заметки:")
created_date=input("дата создания заметки в формате 'день-месяц-год':")
issue_date= input("Дата истечения заметки в формате 'день-месяц-год':")
titles=[]
for i in range(3):
    title=input(f"Введите заголовок заметки {i+1}:")
    titles.append(title)
print("Имя пользователя:",username)
print("Заголовок заметки:",title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
