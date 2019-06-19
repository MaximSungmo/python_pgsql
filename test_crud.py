import psycopg2

import config


def test_insert():
    try:
        conn = psycopg2.connect(**config.db)
        cursor = conn.cursor()
        # cursor.execute('insert into pet values({0}, {1}, {2}, {3}, {4}, default)'
        #                .format('기리기리', 'asd', '시츄', 'm', '2010-01-10'))
        cursor.execute("insert into pet values('기리기리', 'asd', '시츄','m', '2010-01-10', default)")
    except Exception as e:
        print('error: %s' % e)
    finally:
        cursor and cursor.close()
        # commit이 none을 retrun 즉 false,이므로 or를 사용해서 묶어줌
        conn and (conn.commit() or conn.close())

def test_select():
    try:
        conn = psycopg2.connect(**config.db)
        cursor = conn.cursor()
        cursor.execute("select * from pet")
        records = cursor.fetchall()
        for record in records:
            print(record)
    except Exception as e:
        print('error: %s' % e)
    finally:
        cursor and cursor.close()
        # commit이 none을 retrun 즉 false,이므로 or를 사용해서 묶어줌
        conn and (conn.commit() or conn.close())

def test_delete():
    try:
        conn = psycopg2.connect(**config.db)
        cursor = conn.cursor()
        # cursor.execute('insert into pet values({0}, {1}, {2}, {3}, {4}, default)'
        #                .format('기리기리', 'asd', '시츄', 'm', '2010-01-10'))
        cursor.execute("delete from pet where name = '기리기리'")
    except Exception as e:
        print('error: %s' % e)
    finally:
        cursor and cursor.close()
        # commit이 none을 retrun 즉 false,이므로 or를 사용해서 묶어줌
        conn and (conn.commit() or conn.close())


def main():
    test_insert()
    test_select()
    print('=============')
    test_delete()
    test_select()
    print('=============')
    # test_update()
    # test_select()


if __name__ == '__main__':
    main()