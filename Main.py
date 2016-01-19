from Cipher import Cipher


def main():
    cipher = Cipher()
    print "Here are a list of commands which you can perform:\n\t1. encode <string>\n\t2. decode <string>\n\t3. secret <string>\n\t4. print\n\t5. quit\nType your command below:"
    string = None

    while string != "quit":
        string = raw_input("\n")

        if "encode" in string:
            print cipher.encode(string.split("encode ", 1)[1])
        elif "decode" in string:
            print cipher.decode(string.split("decode ", 1)[1])
        elif "secret" in string:
            print cipher.setWord(string.split("secret ", 1)[1])
        elif "print" in string:
            cipher.printGrid()


if __name__ == '__main__':
    main()
