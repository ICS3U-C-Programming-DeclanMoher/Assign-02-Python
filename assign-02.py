def main():
    a = float(input("Enter the a of the kite (cm): "))
    b = float(input("Enter the b of the circle (cm): "))

    area = a * b / 2

    perimeter = 2 * (a + b)

    print("area = {:.2f} cm".format(area))
    print("perimeter = {:.2f} cm".format(perimeter))


if __name__ == "__main__":
    main()
