from dataclasses import dataclass
from turtle import right


class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
