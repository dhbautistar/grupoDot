from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..middlewares.verify_token_route import VerifyTokenRoute
from pydantic import BaseModel

palindromo = APIRouter(route_class=VerifyTokenRoute)

class Palindromo(BaseModel):
    word: str

@palindromo.post("/palindromo")
def palindromos(palindromo: Palindromo):
    palindrome = get_palindrome(palindromo.word)
    return JSONResponse(content=palindrome)

def get_palindrome(str):

    str_length = len(str)
    max_length = 1
    start = 0

    # Marca inicio y final del bucle
    for i in range(str_length):
        for j in range(i, str_length):
            flag = 1

            # Valida el palindromo
            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    flag = 0
 
            # Palindromo
            if (flag != 0 and (j - i + 1) > max_length):
                start = i
                max_length = j - i + 1

    max_length = start + max_length - 1

    response = ''
    for i in range(start, max_length + 1):
        response += str[i]

    # Retorna el palindromo mas largo
    return response
