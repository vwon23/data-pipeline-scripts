#### Import libraries and run initial scripts
import os, sys

from pathlib import Path
from dotenv import load_dotenv

## Find path of the script then find the path of parent folder and add it to system path ##
path_script = os.path.abspath(__file__)
path_app_run = os.path.dirname(os.path.dirname(path_script))
# path_script_dir = Path.cwd()
# path_app_run = os.path.dirname(path_script_dir)

sys.path.append(path_app_run)

## initalize environment variables
dotenv_dir = os.path.dirname(os.path.dirname(path_app_run))
dotenv_path =os.path.join(dotenv_dir, '.env')
load_dotenv(dotenv_path=dotenv_path)

## use common functions to initalize global variable and set logger ##
import utilities.common_functions as cf
#import queries.queries as queries

cf.init(path_app_run)
cf.get_config()
cf.get_current_datetime()

loggername = 'create_environ'
logfile_name = f'{loggername}_{cf.gvar.current_date_pst}.log'
logger = cf.set_logger(loggername, logfile_name)


#### Parse SQL to be exectued
import queries.sf_queries as sf_queries

create_environ_sql = sf_queries.create_environ.format(SF_ADMIN_ROLE=cf.gvar.sf_admin_role,
                                                      SF_DATABASE=cf.gvar.sf_app_db,
                                                      SF_ROLE=cf.gvar.sf_app_role,
                                                      SF_WH=cf.gvar.sf_app_wh)

remove_environ_sql = sf_queries.remove_environ.format(SF_ADMIN_ROLE=cf.gvar.sf_admin_role,
                                                      SF_DATABASE=cf.gvar.sf_app_db,
                                                      SF_ROLE=cf.gvar.sf_app_role,
                                                      SF_WH=cf.gvar.sf_app_wh)

sql = remove_environ_sql
logger.info(f'SQL to be executed:\n {sql}')

#### Connect to Snowflake
cf.connect_snowflake_admin()
# cf.connect_snowflake()

#### Execute SQL and loop through results
cursor_list = cf.gvar.sf_conn.execute_string(sql)

for cursor in cursor_list:
    for row in cursor:
        logger.info(row[0])