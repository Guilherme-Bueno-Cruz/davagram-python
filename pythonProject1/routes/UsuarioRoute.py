from fastapi import APIRouter, Body



router = APIRouter()



@router.post("/", response_description="Rota para criação de novo usuário")
async def rota_criar_usuario(usuario = Body(...)):
    return{
        "mensagem": "usuario criado com sucesso"
    }