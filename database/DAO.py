from database.DB_connect import DBConnect
from model.circuiti import Circuit

class DAO():
    @staticmethod
    def getAllCircuits():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    from circuits"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res
    @staticmethod
    def getAnni():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """SELECT year
        From seasons
        """
        res = []
        cursor.execute(query)
        for row in cursor:
            res.append(row[0])
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getNodi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """
        select *
        from circuits c 
        """
        cursor.execute(query)
        res = []
        for row in cursor:
            circuit = Circuit(**row)
            res.append(circuit)
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getPiloti(y1, y2, circuito):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query= """
        select r.`year`, r2.`position`, r2.driverId 
from races r 
join results r2 on r.raceId = r2.raceId
where r.`year`  >= %s and r.`year` <=%s and r2.`position` is not NULL and r.circuitId = %s
        """
        cursor.execute(query, (y1, y2, circuito))
        res = []
        for row  in cursor:
            res.append(row)
        cursor.close()
        cnx.close()
        return res
    @staticmethod
    def getArchi(y1,y2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = """
        WITH archi AS (
    SELECT r.circuitId, COUNT(res.driverId) AS piloti_validi
    FROM races r
    JOIN results res ON r.raceId = res.raceId
    WHERE r.`year` >= %s AND r.`year` <= %s 
      AND res.`position` IS NOT NULL
    GROUP BY r.circuitId
)
SELECT a1.circuitId, a2.circuitId, (a1.piloti_validi + a2.piloti_validi) AS peso
FROM archi a1
JOIN archi a2 ON a1.circuitId > a2.circuitId
"""
        cursor.execute(query, (y1,y2))
        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res


