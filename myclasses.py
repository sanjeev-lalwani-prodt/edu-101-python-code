from temporalio import workflow


@workflow.defn
class GreetSomeone:
    @workflow.run
    async def run(self, name: str) -> str:
        return f"Hello {name}!"


@workflow.defn
class GreetSanjeev_Someone:
    @workflow.run
    async def run(self,name:str)->str:
        return f"Hello Sanjeev & {name}!!"
    
