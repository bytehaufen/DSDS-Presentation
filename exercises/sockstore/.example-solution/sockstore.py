#!/usr/bin/env python3

# Example Solution for the `Sockenversand-stretched-out` Exercise

class SockStore:
    """
    This class represents a 🧦 sock store. It allows adding socks of different colors,
    searching for socks by color, and buying socks of a specific color.
    """

    def __init__(self):
        """
        Initializes a new instance of the SockStore class.
        """
        self.__socks: dict[str, int] = {}

    def add_sock(self, color: str, quantity: int):
        """
        Adds socks of a specific color to the store.

        Parameters:
        color (str): The color of the socks.
        quantity (int): The quantity of the socks.

        Raises:
        ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Cannot add a negative quantity of socks")
        if color in self.__socks:
            self.__socks[color] += quantity
        else:
            self.__socks[color] = quantity

    def search(self, color: str) -> int:
        """
        Searches for socks of a specific color in the store.

        Parameters:
        color (str): The color of the socks.

        Returns:
        int: The quantity of the socks of the specified color.
        """
        return self.__socks.get(color, 0)

    def buy_sock(self, color: str):
        """
        Buys a sock of a specific color from the store.

        Parameters:
        color (str): The color of the sock.

        Raises:
        ValueError: If there are no socks of the specified color in the store,
                    or if there are no more socks of the specified color left.
        """
        if color not in self.__socks:
            raise ValueError(f"No socks of color {color} available")
        elif self.__socks[color] == 0:
            raise ValueError(f"No more socks of color {color} left")
        else:
            self.__socks[color] -= 1
