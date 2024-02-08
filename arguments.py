import argparse

def main():
    parser = argparse.ArgumentParser(description="Parse string, integer, and float arguments")
    parser.add_argument("string_arg", type=str)
    parser.add_argument("int_arg", type=int)
    parser.add_argument("float_arg", type=float)
    
    args = parser.parse_args()

    string_arg = args.string_arg
    int_arg = args.int_arg
    float_arg = args.float_arg

    print("String:", string_arg)
    print("Int:", int_arg)
    print("Float:", float_arg)

if __name__ == "__main__":
    main()