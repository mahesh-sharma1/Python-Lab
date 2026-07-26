# Lab 1: Model-Based Agent for Vacuum Cleaner World
# Program by: [Your Name]
# Roll no: [Your Roll No]

# Agent's internal memory (model of the world)
world_model = {"A": "Clean", "B": "Clean"}

def model_based_agent(location, status):
    # Update the agent's memory
    world_model[location] = status
    
    # Condition-Action Rules using memory
    if world_model["A"] == "Dirty":
        return "Go to A and Suck"
    elif world_model["B"] == "Dirty":
        return "Go to B and Suck"
    else:
        return "Do Nothing, all locations are clean"

print("********** Model-Based Agent **********\n")
print("Program by: [Mahesh Sharma]")
print("Roll no: [19]\n")

print("Initially, the state model contains:", world_model)

print("\nThe percept sequence is (A, Dirty)")
# action = model_based_agent("A", "Dirty")
print("Action:", model_based_agent("A", "Dirty"))
print("The state model contains:", world_model)

print("\nThe percept sequence is (A, Clean)")
# action = model_based_agent("A", "Clean")
print("Action:", model_based_agent("A", "Clean"))
print("The state model contains:", world_model)

print("\nThe percept sequence is (B, Dirty)")
# action = model_based_agent("B", "Dirty")
print("Action:", model_based_agent("B", "Dirty"))
print("The state model contains:", world_model)

print("\nThe percept sequence is (B, Clean)")
# action = model_based_agent("B", "Clean")
print("Action:",model_based_agent("B", "Clean"))
print("The state model contains:", world_model)