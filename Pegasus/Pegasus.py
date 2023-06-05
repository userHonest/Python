# =============================================#
#   Description: Postgres Database audit
#   Author: u$3r_h0n3$t
#   Date: 02/06/2023
#   Version: 1.0
# =============================================#

# -------<Modules>------------------------------ #
import psycopg2
import argparse
import threading
import pyfiglet 
# ---------------------------------------------- # 

# ================================================================================= # 
# Command-line tool for auditing various aspects of a PostgreSQL database, 
# such as roles, activities, security configurations, default passwords, 
# database size, and long-running transactions
# This script uses multithreading to perform the long transaction audit. 
# The fetch_long_transactions() function is called in a separate thread 
# (threadA) to fetch long-running transactions. If the thread takes too 
# long to complete, a timeout of 15 seconds is set, and the operation is stopped
# note that the audit is recommended to be local 
# ================================================================================= #

banner = pyfiglet.figlet_format("Pegasus")
print(banner)
print("Pegasus PostgreSQL Audit v.1.0\n\n")

# ==== comandline-arguments ===== # 
parser = argparse.ArgumentParser(description='Useful commands to start audit.')
parser.add_argument("-u",dest="user",required=True, help='Database username')
parser.add_argument("-pass", dest="password", required=True, help='Database Password.')
parser.add_argument("-ip", dest="host", required=True, help='Database Host.')
parser.add_argument("-db", dest="database", required=True, help='Database name')

#arguments initiate.
args = parser.parse_args()

credientails = {
    'user': args.user,
    'password': args.password,
    'host': args.host,
    'database': args.database,
}

# ================================================================================= #
# Function to check if the default password is being used on the 'postgres' user
# ================================================================================= # 
def check_default_password():
    
    print("\nChecking for default password on 'postgres' user....")
    
    try:
        default_conn = psycopg2.connect(user='postgres', password='postgres', host=args.host, database=args.database)
        print("Warning:[+] The 'postgres' user has the default password.")
        default_conn.close()
    except psycopg2.OperationalError:
        print("[-] The 'postgres' user does not have the default password.")


try:
    # Connect to the PostgreSQL database using the provided credentials

    conn = psycopg2.connect(**credientails)
    cur = conn.cursor()

    
# ===================================================
#  Function to audit roles and their privileges
# ===================================================
    def audit_roles_and_privileges():
        print("\nAuditing roles and their privileges....")
        cur.execute("""
            SELECT r.rolname, r.rolsuper, r.rolinherit, r.rolcreaterole, r.rolcreatedb, r.rolcanlogin,
                ARRAY(SELECT b.rolname
                        FROM pg_catalog.pg_auth_members m
                        JOIN pg_catalog.pg_roles b ON (m.roleid = b.oid)
                        WHERE m.member = r.oid) as memberof
            FROM pg_catalog.pg_roles r
            WHERE r.rolname !~ '^pg_'
            ORDER BY 1;
        """)
        roles = cur.fetchall()
        for role in roles:
            print(role)
    
     # Function to audit logged activities
    def audit_logged_activities():
        print("\nAuditing logged activities....")
        cur.execute("""
            SELECT query, query_start, state, backend_start, state_change, backend_type
            FROM pg_stat_activity;
        """)
    
        activities = cur.fetchall()
        for activity in activities:
            print(activity)
         
    # Function to audit security configurations
  
    def audit_security_configurations():
        print("\nAuditing security configurations...")
        cur.execute("""
            SELECT name, setting
            FROM pg_settings
            WHERE category = 'Security';
        """)
    
        settings = cur.fetchall()
    
        if not settings:
            print("[-] No security configurations were found")
            return
        
        for setting in settings:
            print(setting)


    # Function to audit database size and growth

    def audit_database_size_and_growth():
        print("\nAuditing database size...")
        cur.execute("""
            SELECT pg_size_pretty(pg_database_size(current_database())) as size;
        """)
        size = cur.fetchone()[0]
        print("[+] Current database size: ", size)

   
    # Function to audit long-running transactions

    def fetch_long_transactions(cur):
        cur.execute("""
        SELECT pid, now() - xact_start AS duration
        FROM pg_stat_activity
        WHERE state IN ('idle in transaction', 'idle in transaction (abandoned)')
        AND now() - xact_start > interval '5 minutes';
        """)

        long_transactions = cur.fetchall()
        if long_transactions:
            for lt in long_transactions:
                print(f"Process {lt[0]} has been in transaction for {lt[1]}")
        else:
            print("[-] No long-running transactions found")
    
    
    # Function to audit long-running transactions and call un the previous function.

    def audit_long_transactions():
        print("\nChecking for long-running long_transactions...")
        threadA = threading.Thread(target=fetch_long_transactions, args=(cur,))
        threadA.start()
        threadA.join(timeout=15)

        if threadA.is_alive():
            print("Taking too long to check for long-running transactions. Operation timed out.")
            threadA._stop()


    ## running all 
    audit_roles_and_privileges()
    audit_logged_activities()
    audit_security_configurations()
    check_default_password()
    audit_database_size_and_growth()
    audit_long_transactions()

    cur.close()
    conn.close()

except psycopg2.OperationalError as e:
    print("Failed to connect to the database. Make sure your IP is whitelisted in pg_hba.conf and your credentials are correct.")
    print("Detailed error: ", e)
    exit(1)

# ========= End Of File =========== # 


