# Arbitary keyword argument : "**" used for arbitary keyword argument, which accept keyword as a dictionary

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

display_info(name="Joshi", age="30", city="Bidar")