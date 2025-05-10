# main.py

from pet import Pet

# Create a Pet named Snowy
snowy = Pet("Snowy")

# Call some methods
snowy.eat()
snowy.sleep()
snowy.play()
snowy.train("sit")
snowy.train("roll over")

# Show tricks
print(f"{snowy.name} knows: {', '.join(snowy.show_tricks())}")

# Show current status
status = snowy.get_status()
print(f"{snowy.name}'s Status:")
print(f"Hunger: {status['hunger']}/10")
print(f"Energy: {status['energy']}/10")
print(f"Happiness: {status['happiness']}/10")
