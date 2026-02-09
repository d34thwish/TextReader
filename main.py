import sys
import time
from collections import Counter


def textTool(file_path):
    counter = Counter()
    line_count = 0
    word_count = 0
    longest_line = ""
    try:
        with open(file_path) as file:
            for line in file:
                line_count += 1
                words = line.split()
                word_count += len(words)
                counter.update(words)
                
                if len(line) > len(longest_line):
                    longest_line = line
        return line_count, word_count, longest_line, counter
    except FileNotFoundError:
            print(f"File not found.")
    except PermissionError:
            print(f"Permission denied.")


if __name__ == "__main__":
    

    start = time.perf_counter()
    

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file_path> [action]")
        print("Actions: read (default), count, longest, top")
        sys.exit(1)

    file_path = sys.argv[1]


    action = sys.argv[2] if len(sys.argv) > 2 else "read"

    if action == "read":
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    print(line.rstrip())
        except FileNotFoundError:
            print(f"File not found.")
        except PermissionError:
            print(f"Permission denied.")
        except UnicodeDecodeError:
            print(f"Could not decode the file at {file_path}. Please ensure it's a text file.") 

    elif action == "count":
        textTool(file_path)
        lines, words, longest, counter = textTool(file_path)
        print(f"Lines: {lines}, Words: {words}")
    elif action == "longest":
        textTool(file_path)
        lines, words, longest, counter = textTool(file_path)
        print(f"Longest line: {longest}")
    elif action == "top":
        try:
            top_n = int(sys.argv[3])
        except (IndexError, ValueError):
            top_n = 5 
        lines, words, longest, counter = textTool(file_path)
        print(f"Top words: {counter.most_common(top_n)}")
    else:
        print(f"Unknown action: {action}")

    print(f"Execution time: {time.perf_counter() - start:.3f} seconds")