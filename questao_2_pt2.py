def list_prof(cursor):
    cursor.execute('SELECT nome FROM professor;')

    professor = cursor.fetchall()

    cursor.close()

    return professor

def exib_info(cursor,prof):
    cursor.execute('SELECT data_nasc, nome_mae, titulacao FROM professor where nome = "{prof}"')

    info = cursor.fetchall()

    cursor.close()

    return info