from passlib.context import CryptContext
from datetime import datetime,timedelta
from jose import jwt 

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str)->str:
    """Hash a plain password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str)->bool:
    """Verify a plain password against its hash."""
    return pwd_context.verify(plain_password,hashed_password)

SECRET_KEY="secrete-key"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

def create_accesstoken(data:dict,expires_delta:timedelta=None)->str:
    """
    Create a JWT access token
    
    Args:
        data:A dictionary of claims (e.g.,{"sub":user id})
        expire_delta:Optional timedelta for expiry

    Returns:
        A JWT access token as a string
    """
    to_encode = data.copy()
    expire=datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_MINUTES))
    to_encode.update({"exp":expire})

    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
