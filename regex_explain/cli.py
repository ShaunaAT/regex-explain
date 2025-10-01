import argparse
from .explainer import explain_regex 


def main():
    parser = argparse.ArgumentParser(description="Explain the given regular expression")
    parser.add_argument("pattern", help="the regex string to explain")
    args = parser.parse_args()

    explanation = explain_regex(args.pattern)
    print(explanation)


if __name__ == "__main__":
    main()