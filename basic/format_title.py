string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"
no_spaces = string_to_process.replace(" ", "")
no_commas = no_spaces.replace(",", " ")
clean_text = no_commas.replace("::", " ")
formatted_title = clean_text.title()
print(f"{formatted_title}")

# Expected Output: The Tale Of Two Cities