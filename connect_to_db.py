
import mysql.connector
import db_conf

def db_connection():
    conf=db_conf.imp_config()
    # print(conf)
            
    dbconnection = mysql.connector.connect(user=conf[1],
                                        password=conf[2],
                                        host=conf[0],
                                        database=conf[3])
    return dbconnection