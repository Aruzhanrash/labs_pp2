import psycopg2

# Подключение к базе данных
print("📡 Подключаемся к БД...")

conn = psycopg2.connect(
    dbname='phonebook_app',
    user='postgres',
    password='12345',
    host='localhost',
    port='5432'
)

cursor = conn.cursor()

def search_by_pattern():
    pattern = input("Введите шаблон для поиска (часть имени или телефона): ")
    cursor.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Ничего не найдено.")

def insert_or_update():
    name = input("Имя: ")
    phone = input("Телефон: ")
    cursor.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    print("Запись добавлена или обновлена.")

def insert_many():
    import json
    print("Вставка нескольких пользователей")
    users = []
    while True:
        name = input("Имя (оставь пустым чтобы закончить): ")
        if not name:
            break
        phone = input("Телефон: ")
        users.append({"name": name, "phone": phone})
    users_json = json.dumps(users)
    cursor.execute("CALL insert_many_users(%s::json);", (users_json,))
    conn.commit()

def paginate():
    limit = int(input("Сколько записей показывать? "))
    offset = int(input("С какого смещения начать? "))
    cursor.execute("SELECT * FROM get_users_page(%s, %s);", (limit, offset))
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")

def delete_user():
    identifier = input("Введите имя или телефон для удаления: ")
    cursor.execute("CALL delete_user(%s, NULL);", (identifier,))


    conn.commit()
    print("Удаление выполнено.")

def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Поиск по шаблону")
        print("2. Добавить или обновить пользователя")
        print("3. Вставить много пользователей")
        print("4. Пагинация")
        print("5. Удалить пользователя")
        print("0. Выход")

        choice = input("Выбери пункт: ")

        if choice == '1':
            search_by_pattern()
        elif choice == '2':
            insert_or_update()
        elif choice == '3':
            insert_many()
        elif choice == '4':
            paginate()
        elif choice == '5':
            delete_user()
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Попробуй снова.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
