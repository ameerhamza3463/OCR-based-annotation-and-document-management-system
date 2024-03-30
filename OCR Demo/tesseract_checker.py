import subprocess

def check_tesseract_installed():
    try:
        subprocess.run(["tesseract", "--version"], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Example usage
if check_tesseract_installed():
    print("Tesseract is installed.")
else:
    print("Tesseract is not installed.")