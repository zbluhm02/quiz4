from dataclasses import dataclass
import math

@dataclass
class Metal:
    name: str
    ppg: float
    weight: float
    
        
def main():
    metals=[
        Metal("gold",50.4,15.3),
        Metal("silver",12.5,102.3),
        Metal("copper",.05, 1000),
        Metal("titanium",1.1, 500.2)
    ]
    val = int(input("Enter the slot you want to check: "))
    print(f"You have ${metals[val].ppg * metals[val].weight} worth of {metals[val].name} in slot {val}")
if __name__=="__main__":
    main()

