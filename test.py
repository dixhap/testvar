import os

def main():
    arm_environment = os.environ.get("ARM_ENVIRONMENT")
    print(f"ARM_ENVIRONMENT variable value: {arm_environment}")

if __name__ == "__main__":
    main()
