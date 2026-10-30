string_to_process = "eggs,cheese,milk,bread,cereal"
capitalized = string_to_process.upper()
thing = capitalized.replace(",", " | ")
print(f"{thing}")

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"