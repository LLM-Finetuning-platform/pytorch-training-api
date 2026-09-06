from src.api.router import BaseRouter

class Router(BaseRouter):
    @staticmethod
    def get_version() -> str:
        return "v1"

V1_router = Router()

@V1_router.register(name="Train")
async def train( model_id: str, peft_id: str ):
    pass 

@V1_router.register(name="Status")
def status(job_id:str):
    pass
    