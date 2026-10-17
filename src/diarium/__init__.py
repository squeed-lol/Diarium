import language_tool_python


def lt_process(input: str):
    tool = language_tool_python.LanguageTool("auto")
    return tool.correct(input)

def main() -> None:
    print("Welcome to Diarium!")
    user_writing = input("Input your writing to have it corrected: ")
    corrected_writing = lt_process(user_writing)
    print(f"\nCorrected text:\n{corrected_writing}")
    input()

if __name__ == "__main__":
    main()
