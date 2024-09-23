# import termcolor
from termcolor import cprint

def run_program():

    while True:
        inp = input("Skrin en röd eller blå:")

        if inp == "röd":
            cprint(inp, color="red")
        elif inp == "blå":
            cprint(inp, color='blue')
        elif inp == "q":
            break
        else:
            pass

if __name__ == "__main__":
    run_program()