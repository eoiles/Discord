def print_rainbow_text(text):
    colors = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
    ]
    reset = "\033[0m"  # Reset color

    for i, char in enumerate(text):
        color = colors[i % len(colors)]  # Cycle through colors
        print(f"{color}{char}{reset}", end="")

    print()  # Move to next line after printing

# Example usage:
print_rainbow_text("Hello, colorful world!")