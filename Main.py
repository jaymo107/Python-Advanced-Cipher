from Cipher import Cipher
import unittest



def main():

    cipher = Cipher()

    print "Here are a list of commands which you can perform:\n\t1. encode <string>\n\t2. decode <string>\n\t3. setsecret <string>\n\t4. quit\nType your command below:"

    string = None

    while string != "quit":
        string = raw_input("\n")

        if len(string) < 10:
            continue

        if "encode" in string:
            print cipher.encode(string.split("encode ", 1)[1])

        elif "decode" in string:
            print cipher.encode(string.split("decode ", 1)[1])

        elif "setsecret" in string:
            pass


if __name__ == '__main__':
    main()
