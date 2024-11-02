# Login to https://xdijbpq-hz01456.snowflakecomputing.com/
# https://ku81904.ap-south-1.aws.snowflakecomputing.com/
# snowflake connection
import snowflake.connector
conn = snowflake.connector.connect(
    user='pruser',
    password='prpassword',
    account='xdijbpq-hz01456',
    warehouse='COMPUTE_WH',
    database='SNOWFLAKE'
)
cur = conn.cursor()
cur.execute("SELECT current_version()")
print(cur.fetchone())
