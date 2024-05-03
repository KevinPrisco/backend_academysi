# "BDtype://user:password@dblocation/Dbname"
# DB_CONNECT = "mysql://root:@localhost/academysibd"
DB_DRIVER = "mysql"
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT: int
DB_NAME = "academysibd"


#JWT TOKEN 
#Generar secret key en el bash -> "rand openssl -hexadecimal 32"
SECRET_KEY = '9c9d3b657b9bb2a65bf1ad60a36f175c306cdc1b41ee8f86e536bcf67e477c5f'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_HOURS = 5
