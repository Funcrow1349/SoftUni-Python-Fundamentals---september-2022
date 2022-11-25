import re
number_of_entries = int(input())

pattern = r"(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)"
for entry in range(number_of_entries):
    current_entry = input()
    barcode = re.search(pattern, current_entry)
    if not barcode:
        print("Invalid barcode")
    else:
        digit_pattern = r"\d"
        extract_nums = re.findall(digit_pattern, barcode.group())
        if not extract_nums:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(extract_nums)}")
