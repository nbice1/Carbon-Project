# Carbon-Project
This program starts by gathering data about the carbon intensity levels in Great Britain due to electricity generation and storing it in a PostgreSQL table named carbon_table. The program is written to store the table in a database named carbon_data, which must first be created by the user in PostgreSQL. The user can of course also change the database name in line 6 of the code. 

The table consists of six columns: id, time_start, time_end, forecasted_carbon, actual_carbon, and carbon_index. Times are divided into half-hour intervals, so each day produces 48 new rows of the table. 

## Set up local environment 

1. Install & start postgres server.

2. Create ```carbon_data``` table. 

3. Run ```python database_setup.py``` to establish table schema in postgres database. 

4. Run ```python carbon.py``` to update database with new rows. 
