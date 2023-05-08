def all_lower(s: str):
    if not s.islower():
        raise "not all lowercase"


all_lower("test")
all_lower("tEst")
