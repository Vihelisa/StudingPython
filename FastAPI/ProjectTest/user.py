class User(BaseModel):
    id: int
    email: str
    senha: str

base_de_dados = [
    User(id=1, email="test@test.com", senha="teste123")
]