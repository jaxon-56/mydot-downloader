<div align="center">

# 🚀 MyDot Downloader

### Download media and post information from **MyDot** with Python.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]()
[![Async](https://img.shields.io/badge/Async-aiohttp-blue?style=for-the-badge)]()

</div>

---

# Install requirements

```bash
pip install -r requirements.txt
```

---

# 💻 Example

```python
import asyncio
from mydot_downloader import MyDotDownloader


async def main():

    async with MyDotDownloader(
        "USERNAME",
        "PASSWORD"
    ) as api:

        post = await api.get_post(
            "https://mydot.one/post/Goodi/status/e6fd5ca8-9c5a-4ed3-842f-19add46f4043"
        )

        print(post)


asyncio.run(main())
```


---

# 📋 Requirements

- Python 3.10+
- aiohttp
- certifi
- aiodot

---

# ⚖ License

Released under the **MIT License**.

---

<div align="center">

Made with ❤️ by **AmirAbbas**

</div>
