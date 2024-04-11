import os

DEFAULT_SESSION_TIMEOUT_SEC = int(os.environ.get("SNOWFLAKE_SESSION_TIMEOUT_SEC", 120))
SNOWFLAKE_ROLE = os.getenv("SNOWFLAKE_ROLE")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_HOST = os.getenv("SNOWFLAKE_HOST")