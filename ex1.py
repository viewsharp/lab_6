import MySQLdb

#! Открытие соединение с базой данных
db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="3298",
    db="lab_db"
)
db.set_character_set('utf8')
#! Получить курсор для работы с базой данных
c=db.cursor()

#! Выполнить вставку
c.execute("insert into labapp_departments (name, description) VALUES (%s, %s);", ('Отдел маркетинга', 'Этаж 4'))
#! Фиксирование изменений
db.commit()

#! Выполнить выборку
c.execute("select * from labapp_departments;")

#! Забрать все полученные записи
entries = c.fetchall()

#! Распечатать записи
for e in entries:
    print(e)

#! Закрытие курсора
c.close()
#! Закрытие соединения
db.close()