"""

Aqui estan las Variables de entorno

normalmente NO se suben y son un archivo .env 
pero para este caso y para ser men


"""

#Variables de conexion con la base de datos
DB_DRIVER = "mysql+aiomysql"
DB_USER = "root"
DB_PASSWORD = "123"
DB_PORT: 3306
DB_HOST = "localhost"
DB_NAME = "academysibd"


#JWT TOKEN 
#Generar secret key en el bash -> "rand openssl -hexadecimal 32"
SECRET_KEY = '9c9d3b657b9bb2a65bf1ad60a36f175c306cdc1b41ee8f86e536bcf67e477c5f'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_HOURS = 5
