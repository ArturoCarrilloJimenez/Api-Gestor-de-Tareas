from dotenv import set_key, load_dotenv
import secrets

def generate_secret_key () :
    load_dotenv()

    secret_key = secrets.token_urlsafe(32) # Genero la clave

    set_key('.env', 'SECRET', secret_key) # La guardo

