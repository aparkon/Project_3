import streamlit as st
from streamlit.elements.number_input import Number
from dataclasses import dataclass
from typing import Any, List


minter_database = {
    "Alex": ["Alex","0x9c9738Ef1308480c0da3E1D83861Db47E7604182","5.0",1, 4],
    "Bailey": ["Baiyley","0x5b57Ca93e29631f22408CC4Cdf7AD5946c5368E5","5.0",2, 3],
    "Jose": ["Jose","0x9d11E92Ae404DEEb04d0A4dbd98C2bD1B795972d","4.8",2, 4],
    "Kian": ["Kian","0x3B025372E0B3b5420335b5c2307C98aD68FADbf5","4.8",2, 3],
    "Melaku": ["Melaku","0x1faBbBd7D5b1Fbe397F54D491420939D84E4c352","4.7",1, 4]
}


