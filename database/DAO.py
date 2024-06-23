from database.DB_connect import DBConnect
from model.prodotto import Prodotto


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(gds.`Date`) as anni
                from go_daily_sales gds 
                order by year(gds.`Date`)"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["anni"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getMetodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct gm.Order_method_type as tipo, gm.Order_method_code as codice
                    from go_methods gm 
                    """

        cursor.execute(query, ())

        for row in cursor:
            result.append((row["codice"], row["tipo"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(anno, metodo):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gds.Product_number as prodotto, sum(gds.Quantity*gds.Unit_sale_price) as somma
                    from go_daily_sales gds 
                    where gds.Order_method_code = %s 
                    and year (gds.`Date`) = %s
                    group by gds.Product_number 
                    """

        cursor.execute(query, (metodo, anno))

        for row in cursor:
            result.append(Prodotto(row["prodotto"], float(row["somma"])))

        cursor.close()
        conn.close()
        return result

