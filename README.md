# 🚀 MyDot Downloader

> An asynchronous Python library for downloading media and retrieving post information from **MyDot**.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Async](https://img.shields.io/badge/Async-aiohttp-orange)

---

## ✨ Features

- ⚡ Fully asynchronous
- 📷 Download photos
- 🎥 Download videos
- 📝 Get post information
- 👤 Get author information
- 🔗 Accept MyDot post URLs
- 📦 Simple API
- 🔒 Automatic SSL fix
- 💙 Built on top of aiodot

---

## 📦 Installation

```bash
git clone https://github.com/jaxon-56/mydot-downloader.git
cd mydot-downloader
pip install -r requirements.txt
```

or

```bash
pip install git+https://github.com/jaxon-56/mydot-downloader.git
```

---

## 📖 Example

```python
import asyncio
from mydot_downloader import MyDotDownloader

async def main():

    api = MyDotDownloader(
        username="USERNAME",
        password="PASSWORD"
    )

    await api.login()

    post = await api.get_post(
        "https://mydot.one/post/Goodi/status/e6fd5ca8-9c5a-4ed3-842f-19add46f4043"
    )

    print(post)

    await api.close()

asyncio.run(main())
```

---

## 📄 Output

```python
{
    "id": "...",
    "short_id": "...",
    "author": "Goodi",
    "text": "Hello",
    "likes": 10,
    "views": 320,
    "media": [
        {
            "type": "video",
            "url": "...",
            "large": "...",
            "thumbnail": "...",
            "duration": 6000
        }
    ]
}
```

---

## ⚙️ Requirements

- Python 3.10+
- aiohttp
- certifi
- aiodot

---

## 🔥 Roadmap

- [x] Login
- [x] Get post
- [x] Get media
- [x] SSL Fix
- [ ] Download media
- [ ] CLI
- [ ] User profile
- [ ] Search
- [ ] Comments
- [ ] Stories

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, don't forget to leave a ⭐ on GitHub.

---

## 👨‍💻 Author

**AmirAbas**

GitHub:
https://github.com/jaxon-56

Repository:
https://github.com/jaxon-56/mydot-downloader
