string_to_process = "  18,27,35,20  "
clean_string = string_to_process.strip()
numbers = [int(num) for num in clean_string.split(",")]
total =sum(numbers)
average = total/len(numbers)
print(f"Total: {total}")
print(f"Average: {average}")

# Expected Output:
# "Total: 100"
# "Average: 25.0"