string_to_process = "   sMitH, aLeX    "
no_spaces = string_to_process.strip()
parts = no_spaces.split(",")
first_name = parts[1].strip().title()
last_name = parts[0].strip().title()
print(f"{first_name} {last_name}")

# Expected output: "Alex Smith"