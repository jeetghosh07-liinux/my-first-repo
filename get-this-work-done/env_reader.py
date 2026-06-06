from dotenv import load_dotenv
import os


def main() -> None:
    load_dotenv()
    print(os.getenv("FAKE_API_KEY"))


if __name__ == "__main__":
    main()

