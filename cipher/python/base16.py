import base64


def main():
    v = input("input\n")
    encoded = v.encode("utf-8")
    b16encoded = base64.b16encode(encoded)
    print(b16encoded)

    decoded = base64.b16decode(b16encoded).decode("utf-8")
    print(decoded)


if __name__ == "__main__":
    main()
