import sqlalchemy
from sqlalchemy import create_engine, text 


db_connection_string= "mysql+pymysql://5v3mib4wz751fz4jwsmc:pscale_pw_4pWOYaW1v1wrcUgIDzYe84CzwZD8IqgEnF5j00pshvB@aws.connect.psdb.cloud/osiriscatalogus?charset=utf8mb4"


engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    } 
  })

from sqlalchemy import create_engine, text



def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_dicts = []

        # Get the column names from the result object
        columns = result.keys()

        for row in result.all():
            row_data = dict(zip(columns, row))
            result_dicts.append(row_data)

        return result_dicts




  

  
    