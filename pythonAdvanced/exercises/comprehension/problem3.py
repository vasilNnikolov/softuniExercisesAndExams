capitals = {country: capital for (country, capital) in zip(input().split(", "), input().split(", "))}
print("\n".join([f"{country} -> {capital}" for (country, capital) in capitals.items()]))

