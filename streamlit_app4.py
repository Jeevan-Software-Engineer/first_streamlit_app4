import snowflake.connector
import streamlit
import pandas
streamlit.title('Zena\'s Amazing Athleisure Catalog')
# connect to snowflake
# def init_connection():
my_cnx = snowflake.connector.Connect(https://firstappapp4-cjsshjqgew65stluachczr.streamlit.app/.Secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
