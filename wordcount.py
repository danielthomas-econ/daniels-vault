import os

def count_words_in_md_files(directories, output_file='word_counts.txt'):
    word_counts = []

    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            word_count = len(content.split())
                            word_counts.append((file_path, word_count))
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

    # Sort files by word count in descending order
    word_counts.sort(key=lambda x: x[1], reverse=True)

    # Output to terminal and to file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_path, count in word_counts:
            line = f"{file_path}: {count} words"
            print(line)
            out_file.write(line + '\n')

        total_words = sum(count for _, count in word_counts)
        summary = f"\n---\nTotal words in all Markdown files: {total_words}"
        print(summary)
        out_file.write(summary + '\n')

# Specify the folders to scan
folders_to_scan = ['Coding', 'Academics']
count_words_in_md_files(folders_to_scan)