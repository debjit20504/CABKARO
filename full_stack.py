import streamlit as st
import mysql.connector as connector

st.set_page_config(page_title="DBMS Project", page_icon=":maple_leaf:", layout="wide")
st.title("Book Ride",)
user_id = st.text_input("User ID")
user_name = st.text_input("Name")
user_phone = st.number_input('Phone no', step = 1)

con = connector.connect(host='localhost', port='3306',user='root',password='Pramanik@12',database='pythontest')
# query = 'create table if not exists user(userId int primary key,userName varchar(200), phone varchar(12))'
# cur = con.cursor()
# cur.execute(query)
# print("Created")

# 	#Insert
if user_phone:
	query = "insert into user(userId,userName,phone) values({},'{}','{}')".format(
		user_id, user_name, user_phone)
	#print(query)
	cur = con.cursor()
	cur.execute(query)
	con.commit()
	print("user saved to db")

	# #Fech All
	# def fetch_all(self):
	# 	query = "select * from user"
	# 	cur = self.con.cursor()
	# 	cur.execute(query)
	# 	for row in cur:
	# 		print("User Id : ", row[0])
	# 		print("User Name :", row[1])
	# 		print("User Phone : ", row[2])
	# 		print()
	# 		print()

	# #delete user
	# def delete_user(self, user_id):
	# 	query = "delete from user where user_id= {}".format(user_id)
	# 	print(query)
	# 	c = self.con.cursor()
	# 	c.execute(query)
	# 	self.con.commit()
	# 	print("deleted")

	# #update

	# def update_user(self, user_id, newName, newPhone):
	# 	query = "update user set user_name='{}',user_phone='{}' where user_id={}".format(
	# 		newName, newPhone, user_id)
	# 	print(query)
	# 	cur = self.con.cursor()
	# 	cur.execute(query)
	# 	self.con.commit()
	# 	print("updated")