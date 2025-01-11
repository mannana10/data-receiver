import sqlite3

connection =sqlite3.connect("mydb.db")
cursor = connection.cursor()

print("""აირჩიეთ რომელი მონაცემის გამოტანა გსურთ ბაზიდან:
        time - თამაშებზე დახარჯული მინიმალური ჯამური დროის მქონე ორი მოთამაშე;
        score - თითო თამაშში მაქსიმალური ქულის მქონე სამი მოთამაშე""")

while True:
    op = input("თქვენი არჩევანი : ").strip().lower()
    if op != "time" and op != "score":
        print("გთხოვთ აირჩიოთ 'time' ან 'score'!")
        continue
    break

def get_data (opt):
    if opt == "time":
        cursor.execute("""SELECT uid, name, sum(games.time) as time
                       FROM games
                       JOIN users ON games.user_id = users.uid
                       GROUP BY user_id
                       ORDER BY time
                       LIMIT 2""")
        data = cursor.fetchmany(2)

    else:
        cursor.execute("""SELECT uid, name, max(games.score) as score
                       FROM games
                       JOIN users ON games.user_id = users.uid
                       GROUP BY user_id
                       ORDER BY score DESC
                       LIMIT 3""")
        data = cursor.fetchmany(3)
    cursor.close()
    connection.close()
    return data


t1 = get_data(op)
for i in t1:
    print(i)