def main() -> None:
    print("Welcome to Diarium!")
    user_writing = input("Input your writing to have it corrected: ")
    correct(user_writing)

def correct(input: str):
    output = input
    print(output)

if __name__ == "__main__":
    main()
