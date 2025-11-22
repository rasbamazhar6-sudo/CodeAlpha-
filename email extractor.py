"""
===========================================================
                  PROFESSIONAL EMAIL EXTRACTOR
===========================================================
DESCRIPTION:
    This automation script scans a text file (email_source.txt),
    extracts all email addresses using Regular Expressions (re),
    removes duplicates, logs progress, and saves results into
    a clean output file (extracted_emails.txt).

FEATURES:
    ✔ Menu-driven interface
    ✔ Error handling for missing files
    ✔ Duplicate email removal
    ✔ Summary report with total and unique emails
    ✔ Professional console output with colors
    ✔ Easy to extend for multiple files or folders
KEY CONCEPTS USED:
    • re (Regular Expressions)
    • File handling
    • Functions & modular design
    • Error handling
===========================================================
"""

import re
import os

# ---------------- COLOR CODES FOR PROFESSIONAL UI ----------------
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ---------------- EMAIL EXTRACTION FUNCTION ----------------
def extract_emails(input_file, output_file):
    """
    Reads a text file, extracts emails, removes duplicates,
    and saves them to a new file.
    """
    print(CYAN + "\n🔍 Starting Email Extraction Process..." + RESET)

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(RED + f"❌ Error: The file '{input_file}' does not exist." + RESET)
        return

    try:
        # Step 1: Read the file content
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
            print(GREEN + f"📄 Successfully read '{input_file}'." + RESET)

        # Step 2: Regex pattern to match emails
        email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        emails = re.findall(email_pattern, text)

        if not emails:
            print(YELLOW + "⚠ No emails found in the file." + RESET)
            return

        # Step 3: Remove duplicates
        unique_emails = sorted(set(emails))

        # Step 4: Save extracted emails to output file
        with open(output_file, "w", encoding="utf-8") as out:
            out.write("======= Extracted Emails =======\n\n")
            for email in unique_emails:
                out.write(email + "\n")
            out.write(f"\nTotal Emails Found: {len(emails)}\n")
            out.write(f"Unique Emails: {len(unique_emails)}\n")

        # Step 5: Summary to console
        print(GREEN + "✅ Email Extraction Completed Successfully!" + RESET)
        print(f"📥 Total emails found: {len(emails)}")
        print(f"✨ Unique emails saved: {len(unique_emails)}")
        print(f"📁 Output file created: {output_file}\n")

    except Exception as e:
        print(RED + "⚠ An error occurred during processing." + RESET)
        print(f"Details: {e}")


# ---------------- MENU SYSTEM ----------------
def menu():
    print(CYAN + """
===========================================================
                   EMAIL EXTRACTION TOOL
===========================================================
Please choose an option:
1. Extract emails from 'email_source.txt'
2. Exit
===========================================================
""" + RESET)


# ---------------- MAIN PROGRAM LOOP ----------------
def main():
    input_file = "email_source.txt"      # Source file
    output_file = "extracted_emails.txt" # Output file

    while True:
        menu()
        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            extract_emails(input_file, output_file)

        elif choice == "2":
            print(GREEN + "\n✔ Program exited successfully. Goodbye!\n" + RESET)
            break

        else:
            print(RED + "❌ Invalid choice! Please enter 1 or 2.\n" + RESET)


# ---------------- START THE PROGRAM ----------------
if __name__ == "__main__":
    main()
