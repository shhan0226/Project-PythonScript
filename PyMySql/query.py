# -*- coding:utf-8 -*-
import pymysql


# DB 접속이 성공시, Connection 객체로부터 cursor() 메서드를 호출
# Cursor 객체의 execute() 메서드를 사용, SQL 문장을 DB 서버에 전송
db = pymysql.connect(host='localhost', port=3306, user='tester', passwd='stack', db='testdb', charset='utf8')

# Cursor Object 호출 ( SQL 실행하기: cursor.execute(SQL) )
# 실행 mysql 서버에 확정 반영하기: db.commit()
# SQL 실행 (Cursor 객체의 execute() 메서드를 사용하여 INSERT, UPDATE 혹은 DELETE 문장을 DB 서버에 보냄)
cursor = db.cursor()
sql = "select * from testtable"
cursor.execute(sql)

# cursor.execute("SHOW TABLES")
sql2 = "INSERT INTO testtable (name,email) VALUES ('CHUSOO', 'CHIN@naver.com');"
cursor.execute(sql2)

sql3 = "select * from testtable"
cursor.execute(sql3)


# DB결과를 모두 호출
result = cursor.fetchall()

# 한번에 다 출력
print(result)

# 레코드별 출력
for row in result:
    print(row)

# 삽입, 갱신, 삭제 등이 모두 끝났으면 Connection 객체의 commit() 메서드를 사용
db.commit()

#Connection 객체의 close() 메서드를 사용하여 DB 연결 종료
db.close()
