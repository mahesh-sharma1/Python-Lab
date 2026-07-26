# Lab : Simple Reflex Agent for Vacuum Cleaner World
# Program by: [Mahesh Sharma]
# Roll no: [19]

def simple_reflex_agent(location, status):
    # location: 'A' or 'B', status: 'Dirty' or 'Clean'
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move to B"
    elif location == "B":
        return "Move to A"
    else:
        return "NoOp"

# Percept Sequences to test
percepts = [
    ("A", "Dirty"),
    ("A", "Clean"),
    ("B", "Dirty"),
    ("B", "Clean")
]

print("********** Simple Reflex Agent **********\n")
print("Program by: [Mahesh Sharma]")
print("Roll no: [19]\n")

for percept in percepts:
    location, status = percept
    action = simple_reflex_agent(location, status)
    print(f"Percept: Location={location}, Status={status} → Action: {action}")