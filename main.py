import sys
import asyncio
from myclasses import GreetSanjeev_Someone, GreetSomeone

async def main():
    name = sys.argv[1]
    greeter = GreetSomeone()
    greeting = await greeter.run(name)
    print(greeting)
    slgreeter = GreetSanjeev_Someone()

    slgreeting1 = await slgreeter.run(name)
    print(slgreeting1)


if __name__ == "__main__":
    asyncio.run(main())
