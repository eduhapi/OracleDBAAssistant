import cx_Oracle

def connect_to_oracle(instance):
    """Establish a connection to the Oracle database using provided instance details."""
    try:
        connection = cx_Oracle.connect(user=instance.username, password=instance.password, dsn=instance.dsn)
        return connection
    except cx_Oracle.DatabaseError as e:
        raise Exception(f"Database connection error: {e}")

def get_instance_details(connection):
    """Fetch important details from the Oracle database."""
    details = {}
    try:
        cursor = connection.cursor()
        
        # Example query to get Oracle version info
        cursor.execute("SELECT * FROM v$version")
        details['version_info'] = cursor.fetchall()

        # Example query to get tablespace sizes
        cursor.execute("SELECT tablespace_name, bytes/1024/1024 AS size_mb FROM dba_data_files")
        details['tablespace_info'] = cursor.fetchall()

    except cx_Oracle.DatabaseError as e:
        raise Exception(f"Error fetching instance details: {e}")
    finally:
        cursor.close()
    
    return details

def perform_db_tasks(instance):
    """Perform DBA tasks on the provided Oracle instance."""
    connection = None
    cursor = None
    try:
        connection = connect_to_oracle(instance)
        cursor = connection.cursor()

        # Example: Rebuild indexes
        cursor.execute("""
            BEGIN
                FOR rec IN (SELECT index_name, table_name FROM user_indexes WHERE status = 'UNUSABLE') LOOP
                    EXECUTE IMMEDIATE 'ALTER INDEX ' || rec.index_name || ' REBUILD';
                END LOOP;
            END;
        """)

        # Add more DBA tasks here as needed
        
    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
import cx_Oracle

def connect_to_oracle(instance):
    try:
        connection = cx_Oracle.connect(user=instance.username, password=instance.password, dsn=instance.dsn)
        return connection
    except cx_Oracle.DatabaseError as e:
        print(f"Database error: {e}")
        return None

def get_tablespace_usage(instance):
    connection = connect_to_oracle(instance)
    if not connection:
        return []

    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT tablespace_name, round(space_used / space_total * 100, 2) as usage_percentage
            FROM (
                SELECT tablespace_name,
                       SUM(bytes) / 1024 / 1024 AS space_total,
                       SUM(decode(free_space, NULL, 0, free_space)) / 1024 / 1024 AS space_used
                FROM dba_tablespaces
                LEFT JOIN dba_free_space
                ON dba_tablespaces.tablespace_name = dba_free_space.tablespace_name
                GROUP BY tablespace_name
            )
        """)
        result = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
    
    return result

def get_active_sessions(instance):
    connection = connect_to_oracle(instance)
    if not connection:
        return []

    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT sid, serial#, username, status, program
            FROM v$session
            WHERE status = 'ACTIVE'
        """)
        result = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

    return result

def get_dba_users(instance):
    connection = connect_to_oracle(instance)
    if not connection:
        return []

    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT username, account_status, default_tablespace
            FROM dba_users
        """)
        result = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

    return result
import cx_Oracle

def get_performance_metrics(instance):
    metrics = {}
    connection = None
    cursor = None
    
    try:
        connection = cx_Oracle.connect(user=instance.username, password=instance.password, dsn=instance.dsn)
        cursor = connection.cursor()

        queries = {
            "CPU Usage": """
                SELECT
                    ROUND((1 - (VALUE / (SELECT VALUE FROM V$SYSSTAT WHERE NAME = 'IDLE TIME'))) * 100, 2) AS CPU_Usage
                FROM
                    V$SYSSTAT
                WHERE
                    NAME = 'CPU TIME'
            """,
            "Memory Usage": """
                SELECT
                    ROUND((SUM(VALUE) / (1024 * 1024)), 2) AS Memory_Usage_MB
                FROM
                    V$SGAINFO
                WHERE
                    NAME = 'Total SGA Size'
            """,
            "Active Sessions": """
                SELECT
                    COUNT(*) AS Active_Sessions
                FROM
                    V$SESSION
                WHERE
                    STATUS = 'ACTIVE'
            """
        }

        for metric, query in queries.items():
            cursor.execute(query)
            result = cursor.fetchone()
            metrics[metric] = result[0] if result else 'N/A'

    except cx_Oracle.DatabaseError as e:
        metrics['Error'] = str(e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return metrics
