import os


def run_setup():
    required_dirs = ["./uploads"]
    for dir in required_dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)
            print(f"Created '{dir}' directory.")
