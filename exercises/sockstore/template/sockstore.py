#!/usr/bin/env python3


class SockStore:
    def __init__(self):
        self.__socks: dict[str, int] = {}

    def add_sock(self, color: str, quantity: int):
        pass

    def search(self, color: str) -> int:
        return 42

    def buy_sock(self, color: str):
        pass
