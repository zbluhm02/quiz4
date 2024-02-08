from typing import List
from dataclasses import dataclass
import math


@dataclass
class Metal:
    name: str
    ppg: float
    weight: float
    
def search_metal_array(arr: List[Metal], name_to_search: str) -> int:
    for i, metal in enumerate(arr):
        if metal.name == name_to_search:
            return "We have that metal in stock"
    return "We don't have that metal in stock"
        
def main():
    metals=[
        Metal("gold",50.4,15.3),
        Metal("silver",12.5,102.3),
        Metal("copper",.05, 1000),
        Metal("titanium",1.1, 500.2)
    ]
    otherotherval = input("Enter a metal to check if we have it in stock: ")
    otherval = search_metal_array(metals, otherotherval)
    print (otherval)
    
    val = int(input("Enter the slot you want to check: "))
    print(f"You have ${metals[val].ppg * metals[val].weight} worth of {metals[val].name} in slot {val}")
    
    
if __name__=="__main__":
    main()

