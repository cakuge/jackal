import os
import sys
import jackal

def main():
    with open("passwords.txt", "r") as f:
        passwords = f.read().splitlines()
    unique_words = set(passwords)
    with open("jackal_results.txt", "w") as f:
        for word in unique_words:
            f.write(word + "\n")
            

if __name__ == "__main__":
    main()
    if os.path.exists("passwords.txt"):
        os.remove("passwords.txt")