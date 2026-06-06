def print_history(messages: list[str]) -> None:
    if not messages:
        print("No messages yet.")
        return

    print("\nFull chat history:")
    for index, message in enumerate(messages, start=1):
        print(f"{index}. {message}")
    print()


def main() -> None:
    messages: list[str] = []

    while True:
        user_input = input("Enter a message ('history' or 'quit'): ").strip()
        command = user_input.lower()

        if command == "quit":
            print("Goodbye!")
            break

        if command == "history":
            print_history(messages)
            continue

        if user_input:
            messages.append(user_input)
            print(f"Saved message #{len(messages)}.")


if __name__ == "__main__":
    main()

