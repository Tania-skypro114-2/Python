from sqlalchemy import create_engine, text


connection_string = "postgresql://postgres:13znenf@localhost:5432/postgres"
pg = create_engine(connection_string)


def test_insert_new_subject():
    connection = pg.connect()
    transaction = connection.begin()
    sql = text("insert into subject (subject_id, subject_title)"
               "values (:new_id, :new_title)")
    connection.execute(sql, {'new_id': 18, 'new_title': 'Logik'})
    sql = text("SELECT subject_title FROM subject WHERE subject_id = :new_id")
    result = connection.execute(sql, {'new_id': 18})
    new_subject = result.fetchone()[0]
    assert new_subject == 'Logik'
    sql = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql, {"new_id": 18})
    transaction.commit()
    connection.close()


def test_update_subject():
    connection = pg.connect()
    transaction = connection.begin()
    sql = text("insert into subject (subject_id, subject_title)"
               "values (:new_id, :new_title)")
    connection.execute(sql, {'new_id': 18, 'new_title': 'Logik'})
    sql = text("UPDATE subject SET subject_title = :updated_title "
               "WHERE subject_id = :new_id")
    connection.execute(sql, {'updated_title': 'Classic lit', 'new_id': 18})
    sql = text("SELECT subject_title FROM subject WHERE subject_id = :new_id")
    result = connection.execute(sql, {'new_id': 18})
    updated_title = result.fetchone()[0]
    assert updated_title == 'Classic lit'
    sql = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql, {"new_id": 18})
    transaction.commit()
    connection.close()


def test_delete_subject():
    connection = pg.connect()
    transaction = connection.begin()
    in_count = connection.execute(text
                                  ("SELECT COUNT(*) FROM subject")).scalar()
    sql = text("insert into subject "
               "(subject_id, subject_title) values (:new_id, :new_title)")
    connection.execute(sql, {'new_id': 18, 'new_title': 'Logik'})
    sql = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql, {"new_id": 18})
    fin_count = connection.execute(text
                                   ("SELECT COUNT(*) FROM subject")).scalar()
    assert in_count == fin_count
    transaction.commit()
    connection.close()
