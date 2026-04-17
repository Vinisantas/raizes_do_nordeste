

from pydantic import BaseModel


class Token(BaseModel):
    token_acesso: str  
    token_tipo: str 