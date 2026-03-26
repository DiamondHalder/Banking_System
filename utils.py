from __future__ import annotations

def prompt_non_empty(prompt: str) -> str:
    
    while True:
        s = input(prompt).strip()
        if s:
            return s
        else:
            print("Error: Empty input is not allowed. Please try again.")

def clean_name(raw_name: str) -> str:
   
    return raw_name.strip().title()

def prompt_int(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
   
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Error: Please enter a valid integer number.")
            continue

        if min_val is not None and val < min_val:
            print(f"Error: Value must be at least {min_val}")
            continue
        if max_val is not None and val > max_val:
            print(f"Error: Value must be no more than {max_val}")
            continue

        return val