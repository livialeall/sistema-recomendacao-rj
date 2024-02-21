import sqlite3
from faker import Faker

#conecção com db
conn = sqlite3.connect(r'C:\Users\livia\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db')
cursor = conn.cursor()
print(conn)

#instancia do faker
fake = Faker()

#dados ficticios
for _ in range(5000):
    user_gender = fake.random_element(elements=('M','F'))
    user_name = fake.name()
    user_email = fake.email()
    user_preference_time = fake.random_element(elements=('Diurno','Vespertino','Noturno'))
    user_preference_role = fake.random_element(elements=(' Ao ar livre', 'Restaurantes e Bares', 'Compras/Feirinhas', 'Shows e Música ao vivo', 'Festas e Baladas', ' Peças', 'Cinema'))
    user_preference_price = fake.random_int(min=1,max=5)
    user_preference_area = fake.random_element(elements=('ZO','ZS','ZN','Centro'))
    user_public = fake.random_element(elements=( 'amigos', 'infantil', 'juvenil', 'romantico', 'solo'))
    cursor.execute(
        'INSERT INTO tb_users (user_gender,user_name,user_email,user_preference_time,user_preference_role,user_preference_price,user_preference_area,user_public) VALUES (?,?,?,?,?,?,?,?);', (user_gender,user_name,user_email,user_preference_time,user_preference_role,user_preference_price,user_preference_area,user_public))

conn.commit()

conn.close()