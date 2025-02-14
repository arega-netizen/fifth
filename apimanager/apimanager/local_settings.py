SECRET_KEY = "abc"

API_HOST = "http://127.0.0.1:8080/"

OAUTH_CONSUMER_KEY = 'fsruzredonfxcyieofn1bzbf2hrh5irtm2ubrkyn'
OAUTH_CONSUMER_SECRET = 'ulpsrngnro2l3dxxvyh50l4mh0dr4el1e4s40r5u'
# Database filename, default is `../db.sqlite3` relative to this file


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'obpdb',  # Name of the database
        'USER': 'guest',    # Database username
        'PASSWORD': 'catsarecool',  # Database password
        'HOST': 'localhost',        # Database host (e.g., 'localhost' or an IP address)
        'PORT': '1433',                # Default port for MSSQL
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # ODBC driver for MSSQL
        },
    }
}