from PIL import Image


def main():

    l = Image.open("1.jpg")
    l = l.resize((512,512), Image.NEAREST)
    c = Image.open("5.jpg")
    c = c.resize((512,512), Image.NEAREST)

    print(type(l))

    l.show()
    c.show()
    l.save("ladySmall.jpg")
    c.save("cosmoSmall.jpg")


if __name__ == "__main__":
    main()
