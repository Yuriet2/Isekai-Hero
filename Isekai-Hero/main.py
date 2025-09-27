---

### 3. `main.py`
```python
import asyncio
from bots.main_bot import start_bot
from backend.main import start_backend

async def main():
    # Iniciar backend y bot en paralelo
    await asyncio.gather(
        start_backend(),
        start_bot()
    )

if __name__ == "__main__":
    asyncio.run(main())
