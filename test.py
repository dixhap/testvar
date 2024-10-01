import os

def main():
    my_variable = os.getenv('MY_VARIABLE')
    print(f"MY_VARIABLE value: {my_variable}")

if __name__ == "__main__":
    main()
