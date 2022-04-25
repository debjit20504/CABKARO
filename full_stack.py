import mysql.connector as c
import streamlit as st
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from random import randint

con=c.connect(host="localhost", user="root", passwd="Pramanik@12", database="dbms_project",port="3306")
st.set_page_config(page_title="DBMS Project", page_icon=":maple_leaf:", layout="wide")

nav = st.sidebar.radio("Navigation", ["Home", "SignUp/ Login"])
if nav == "SignUp/ Login":
    st.title("Signup/ Login Page")
    login = st.selectbox("How do you want to login?", ["Signup as Customer", "Login as Customer", "Login as Administrator"])
    if login == "Login as Customer":
        st.text_input("Username: ")
        st.text_input("Password: ", type="password")
        c1,c2 = st.columns([7,1])
        c2.button("Submit")

    if login == "Signup as Customer":
        # query = "select cust_id from customer"
        # cur = con.cursor()
        # cur.execute(query)
        # data = cur.fetchall()
        # st.write(data)
        first, last = st.columns(2)
        first.text_input("First name")
        last.text_input("Last name")
        passw, phno = st.columns([3, 1])
        passw.text_input("Password: ", type="password")
        phno.text_input("Phone number")
        # list = []
        # for i in range(len(data)):
        #     list.append(data[i][0])
        # while(True):
        #     n = randint(10000, 99999)
        #     if n not in list:
        #         break
        #     else:
        #         continue
        c1, c2 = st.columns([7, 1])
        if c2.button("Submit"):
            st.success("You have been successfully registered")
            st.success("Now you can go to HomePage")

if nav == "Home":
    with st.container():
        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        # Use local CSS
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/style.css")

        # ---- LOAD ASSETS ----
        lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_hsabbeks.json")
        lottie_coding_email = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_5wr08scz.json")

        # ---- HEADER SECTION ----
        with st.container():
            title_container = st.container()
            col1, col2 = st.columns([1, 20])
            image = Image.open('images\\CabHUB.png')
            with title_container:
                with col1:
                    st.image(image, width=64)
            st.markdown("<h1 style='text-align: center; color: orange;'>Book a Taxi in your city</h1>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: center; color: black;'>choose from a range of categories and prices</h6>", unsafe_allow_html=True)

        # ---- WHAT I DO ----
        with st.container():
            st.write("---")
            left_column,right_column = st.columns(2)
            with left_column:
                st.header("Book a Ride")
                left_column.text_input("Pick up")
                left_column.text_input("Drop")
                option = st.selectbox('Car type',('Mini', 'Prime Sedan', 'Auto', 'Prime Play', 'Prime Suv'))
                st.write('You selected:', option)
            with right_column:
                st_lottie(lottie_coding, height=600, key="coding")

        # ---- CONTACT ----
        with st.container():
            st.write("---")
            st.header("Get In Touch With Me!")
            st.write("##")

            # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
            contact_form = """
            <form action="https://formsubmit.co/debjit20504@iiitd.ac.in.COM" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st_lottie(lottie_coding_email, height=300, key="email")
