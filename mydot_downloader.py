"""
MyDot Downloader
~~~~~~~~~~~~~~~~

Async MyDot Downloader

Author  : AmirAbas
GitHub  : https://github.com/jaxon-56/mydot-downloader
License : MIT
"""

from __future__ import annotations

import re
import ssl
import certifi
import aiohttp

from typing import Any
from aiodot import MyDotClient

__title__ = "mydot-downloader"
__version__ = "1.0.0"
__author__ = "AmirAbas"
__license__ = "MIT"

# ==========================================================
# SSL Fix
# ==========================================================

_ssl_context = ssl.create_default_context(cafile=certifi.where())

_original_session = aiohttp.ClientSession


def _patched_session(*args, **kwargs):
    kwargs.setdefault(
        "connector",
        aiohttp.TCPConnector(
            ssl=_ssl_context
        ),
    )
    return _original_session(*args, **kwargs)


aiohttp.ClientSession = _patched_session

# ==========================================================
# Exceptions
# ==========================================================


class InvalidLink(ValueError):
    pass


class LoginRequired(RuntimeError):
    pass


# ==========================================================
# Downloader
# ==========================================================


class MyDotDownloader:
    """
    Async MyDot Downloader
    """

    def __init__(
        self,
        username: str,
        password: str,
        session_file: str = "session.json",
    ):

        self.username = username
        self.password = password
        self.session_file = session_file

        self.client: MyDotClient | None = None

    async def __aenter__(self):
        await self.login()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def login(self) -> None:
        self.client = MyDotClient(
            session_file=self.session_file
        )

        await self.client.__aenter__()

        await self.client.login(
            self.username,
            self.password,
        )

    async def close(self) -> None:
        if self.client:
            await self.client.__aexit__(
                None,
                None,
                None,
            )

    @staticmethod
    def extract_id(value: str) -> str:

        value = value.strip()

        match = re.search(
            r"status/([0-9a-fA-F\-]+)",
            value,
        )

        if match:
            return match.group(1)

        if re.fullmatch(
            r"[0-9a-fA-F\-]{36}",
            value,
        ):
            return value

        raise InvalidLink(
            "Invalid MyDot post URL."
        )

    async def get_post(
        self,
        link: str,
    ) -> dict[str, Any]:

        if self.client is None:
            raise LoginRequired(
                "You must login first."
            )

        dot = await self.client.get_dot(
            self.extract_id(link)
        )

        return {

            "id": dot.id,
            "short_id": dot.short_id,
            "text": dot.content,
            "type": dot.dot_type,
            "created_at": dot.created_at,

            "likes": dot.likes_count,
            "views": dot.view_count,
            "replies": dot.replies_count,
            "reposts": dot.reposts_count,
            "quotes": dot.quotes_count,
            "bookmarks": dot.bookmarks_count,

            "author": dot.author,

            "media": [

                {

                    "id": media.get("media_id"),

                    "type": media.get(
                        "media_type"
                    ),

                    "mime_type": media.get(
                        "mime_type"
                    ),

                    "url": media.get("url"),

                    "thumbnail": media.get(
                        "thumbnail_url"
                    ),

                    "small": media.get(
                        "small_url"
                    ),

                    "medium": media.get(
                        "medium_url"
                    ),

                    "large": media.get(
                        "large_url"
                    ),

                    "hls": media.get(
                        "hls_url"
                    ),

                    "width": media.get(
                        "width"
                    ),

                    "height": media.get(
                        "height"
                    ),

                    "size": media.get(
                        "size"
                    ),

                    "duration_ms": media.get(
                        "duration_ms"
                    ),

                }

                for media in dot.media

            ],

        }

    async def get_media(
        self,
        link: str,
    ) -> list[dict]:

        return (
            await self.get_post(link)
        )["media"]

    async def get_author(
        self,
        link: str,
    ) -> dict:

        return (
            await self.get_post(link)
        )["author"]

    async def get_text(
        self,
        link: str,
    ) -> str:

        return (
            await self.get_post(link)
        )["text"]

    async def get_views(
        self,
        link: str,
    ) -> int:

        return (
            await self.get_post(link)
        )["views"]

    async def get_likes(
        self,
        link: str,
    ) -> int:

        return (
            await self.get_post(link)
        )["likes"]
