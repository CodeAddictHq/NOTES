# Nested if: if statements inside other if statements

age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID required.")
else:
    print("Must be 18 or older.")

# Avoid deep nesting when possible — use 'and' instead
if age >= 18 and has_id:
    print("Entry allowed (cleaner version).")
