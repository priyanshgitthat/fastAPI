# auth.hash.py

from passlib.context import CryptContext

# Use bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash plain password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Function to verify a plain password against a hashed one
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
