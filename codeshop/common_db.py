#coding:utf-8

from django.db import connection
from django.db import transaction
from django.utils.encoding import smart_text
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print(sys.path)


#auto_increment
#@transaction.atomic
def custom_sql(sql):
    #sql=sql.decode('utf8')
    #cursor = connection.cursor(cursorclass = MySQLdb.cursors.DictCursor)
    cursor = connection.cursor()
    #print sql
    cursor.execute(sql)
    #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    #data = cursor.fetchall()
    columns = [d[0] for d in cursor.description]
    #list_data=[[item for item in row]  for row in cursor.fetchall()]
    data = [dict(zip(columns, row))  for row in cursor.fetchall()]
    #print(data)
    return data




# single_sql
def single_sql(sql):
    cursor = connection.cursor()
    #print sql
    cursor.execute(sql)
    columns = [d[0] for d in cursor.description]
    #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    data = [dict(zip(columns, row))  for row in cursor.fetchall()]
    return data

# single_sql
def single_column_sql(sql):
    cursor = connection.cursor()
    #print sql
    cursor.execute(sql)
    data =cursor.fetchone()
    return data



#execute dml
def excute_sql(sql):
    cursor = connection.cursor()
    n=cursor.execute(sql)
    transaction.commit()
    return n

#insert

def insert_sql(sql):
    cursor = connection.cursor()
    flag=cursor.execute(sql)
    if flag==1:
        #newest insert idcursor.lastrowid
        n=cursor.lastrowid
    else:
        n=0
    return n


#dml_sql
def dml_sql(table_name,column,values):
    cursor = connection.cursor()
    #print "insert into "+table_name+"("+column+") values("+values+")"
    n=cursor.execute("insert into "+table_name+"("+column+") values("+values+")")
    transaction.commit()
    return n



#dml_sql_insert
def dml_sql_insert(table_name,column,values):
    cursor = connection.cursor()
    #print 	table_name

    #print column
    #print values
    #print "insert into "+table_name+" ("+column+") values("+values+")"
    flag=cursor.execute("insert into "+table_name+"("+column+") values("+values+")")
    if flag==1:
        #newest insert idcursor.lastrowid
        n=cursor.lastrowid
    else:
        n=0
    transaction.commit()
    return n

#dml_sql_insert_para
def dml_sql_insert_para(table_name,column,values,*arg):
    cursor = connection.cursor()
    sql="\""+"insert into "+table_name+"("+column+") values("+values+")"+"\""
    sql=sql % (arg)
    #print sql
    flag=cursor.execute(sql)
    if flag==1:
        #newest insert idcursor.lastrowid
        n=cursor.lastrowid
    else:
        n=0
    transaction.commit()
    return n


#dml_sql_insert_para
def dml_sql_insert_val(sql):
    cursor = connection.cursor()
    #print sql
    flag=cursor.execute(sql)
    if flag==1:
        #newest insert idcursor.lastrowid
        n=cursor.lastrowid
    else:
        n=0
    transaction.commit()
    return n



#update_sql
def update_sql(table_name,set_sql,where_con):
    cursor = connection.cursor()
    #print "update "+table_name+" set "+set_sql+" where "+where_con
    n=cursor.execute("update "+table_name+" set "+set_sql+" where "+where_con)
    transaction.commit()
    #transaction.commit_unless_managed()
    return n



#update_sql_para
def update_sql_para(sql):
    cursor = connection.cursor()
    #print sql
    n=cursor.execute(sql)
    transaction.commit()
    #transaction.commit_unless_managed()
    return n
#delete_sql
def delete_sql(table_name,where_con):
    cursor = connection.cursor()
    #print "insert into "+table_name+"("+column+") values("+values+")"
    n=cursor.execute("delete from  "+table_name+" where "+where_con)
    transaction.commit()
    return n

def getUser(user_id):
    user_info=single_sql("select user_id,user_name,introduce,avatar from users where user_id="+str(user_id))
    author=[]
    author_list={}
    author_list['user_id']=user_info[0]
    author_list['user_name']=user_info[1]
    author_list['introduce']=user_info[2]
    author_list['avatar']=user_info[3]
    author.append(author_list)
    return author