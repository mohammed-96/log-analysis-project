import psycopg2

conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()

cursor.execute(
    "SELECT DISTINCT(SUBSTRING(path ,10 )) AS slug , COUNT(id)"
    "FROM log WHERE status = '200 OK' AND SUBSTRING(path ,10 ) != ''"
    "GROUP BY slug ORDER BY count DESC LIMIT 3 ;"
)

results = cursor.fetchall()
print("Q1: ")
print("'" + str(results[0][0]) + "' - " + str(results[0][1]) + " views")
print("'" + str(results[1][0]) + "' - " + str(results[1][1]) + " views")
print("'" + str(results[2][0]) + "' - " + str(results[2][1]) + " views")

cursor.execute(
    "SELECT c.name AuthorName, SUM(p.freq)NumOfView FROM articles a "
    "LEFT JOIN authors c ON c.id = a.author "
    "LEFT JOIN (SELECT SUBSTRING(path ,10 ) AS path ,"
    "COUNT(*) AS freq FROM log GROUP BY path) p ON p.path = a.slug "
    "GROUP BY c.name ORDER BY SUM(p.freq) DESC ;"
)

results = cursor.fetchall()
print("Q2: ")
print("'" + str(results[0][0]) + "' - " + str(results[0][1]) + " views")
print("'" + str(results[1][0]) + "' - " + str(results[1][1]) + " views")
print("'" + str(results[2][0]) + "' - " + str(results[2][1]) + " views")
print("'" + str(results[3][0]) + "' - " + str(results[3][1]) + " views")


cursor.execute(
    "SELECT TO_CHAR(DATE(time) , 'Mon DD ,YYYY') AS date "
    ",ROUND((100.0 * SUM(CASE WHEN status NOT LIKE '2%' THEN 1 "
    "ELSE 0 END)  / COUNT(*)) , 2) AS perc  FROM log GROUP BY DATE(time) "
    "ORDER BY perc DESC LIMIT 1 ;"
)

results = cursor.fetchall()
print("Q3: ")
print(str(results[0][0]) + "' - " + str(results[0][1]) + "% Errors")

conn.close()
