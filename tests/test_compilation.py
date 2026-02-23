import os
import sys

# Add paths to sys.path so we can import wb_config
sys.path.append(os.path.join(os.getcwd(), 'AA'))

def check_compilation(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        compile(content, filepath, 'exec')
        return True
    except Exception as e:
        print(f"Compilation error in {filepath}: {e}")
        return False

def check_wb_config_usage(filepath):
    # Skip wb_config itself and empty files
    if filepath.endswith("wb_config.py"):
        return True

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if wb_config is imported if used
        if "wb_config." in content and "import wb_config" not in content and "from wb_config import" not in content:
            print(f"Error in {filepath}: uses wb_config but does not import it.")
            return False

        return True
    except Exception as e:
        print(f"Check error in {filepath}: {e}")
        return False

def main():
    failed_files = []

    # Check AA/
    for root, dirs, files in os.walk("AA"):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                if not check_compilation(filepath):
                    failed_files.append(filepath)
                if not check_wb_config_usage(filepath):
                    failed_files.append(filepath)

    # Check DemoCode/
    for root, dirs, files in os.walk("DemoCode"):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                if not check_compilation(filepath):
                    failed_files.append(filepath)
                if not check_wb_config_usage(filepath):
                    failed_files.append(filepath)

    if failed_files:
        print(f"Found {len(failed_files)} files with errors.")
        sys.exit(1)
    else:
        print("All files compiled successfully and config usage looks correct.")
        sys.exit(0)

if __name__ == "__main__":
    main()
