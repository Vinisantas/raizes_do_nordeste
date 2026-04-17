from pwdlib import PasswordHash
pwd_context = PasswordHash.recommended()

#função de buscar password
def busca_senha_hash(password: str):
    return pwd_context.hash(password)



#função de verificar password
def verifica_senha(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)