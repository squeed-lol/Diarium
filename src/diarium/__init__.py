import language_tool_python
import rich


class CorrectionProcessor:
    def __init__(self, input_text : str) -> None:
        self.input_text = input_text
        self.tool = language_tool_python.LanguageTool("auto")
        self.matches = self.tool.check(input_text)
        self.corrected_text = self.tool.correct(input_text)

# legacy
def lt_process(input: str):
    tool = language_tool_python.LanguageTool("auto")
    return tool.correct(input)

def main() -> None:
    print("Welcome to Diarium!")
    user_writing = input("Input your writing to have it corrected: ")
    corrected_writing = CorrectionProcessor(user_writing).corrected_text
    print(f"\nCorrected text:\n{corrected_writing}")
    input()

if __name__ == "__main__":
    main()
