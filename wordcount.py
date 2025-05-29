import os

def count_words_in_md_files(directories):
    total_words = 0  # To accumulate total word count

    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            word_count = len(content.split())
                            total_words += word_count
                            print(f"{file_path}: {word_count} words")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

    print("\n---")
    print(f"Total words in all Markdown files: {total_words}")

# Specify the folders to scan
folders_to_scan = ['Coding', 'College work']
count_words_in_md_files(folders_to_scan)