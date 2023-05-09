from static import dictionary, special_symbols


def make_translite(text: str) -> str:
    if not text:
        return text
    return "".join(
        [
            "" if sign in special_symbols or (i > 0 and text[i - 1] == " " and sign == " ")
            else dictionary.get(sign, sign)
            for i, sign in enumerate(text.strip().lower())
        ]
    )


def main():
    text = input("TEXT: ")
    new_text = make_translite(text)
    print("NEW TEXT: ", new_text)


if __name__ == '__main__':
    main()
