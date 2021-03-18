class Config:
    
    USER= 'postgres'
    PASS = 'admin'
    HOST = 'localhost'
    NAME_DB='COBRA1'
    FULL_URL = f'postgresql://{USER}:{PASS}@{HOST}/{NAME_DB}'
    
    SECRET_KEY = 'itsasecret'
    SQLALCHEMY_DATABASE_URI=FULL_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    