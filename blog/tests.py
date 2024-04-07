from sqlite3 import Connection

connection =Connection('../db.sqlite3')
cursor = connection.cursor()
query = """ create table contact(
    id bigserial primary key,
    name varchar(128),
    mesasage text,
    created_at timestamp default CURRENT_TIMESTAMP
);
"""
cursor.execute("""insert into contact(name) values('Javlon'),('Borya')""")
connection.commit()