from argparse import ArgumentParser
import sys
import time
from collections import Counter


def text_tool(file_path):
    counter = Counter()
    line_count = 0
    word_count = 0
    longest_line = ""
    try:
        with open(file_path, encoding='utf-8') as file:
            for line in file:
                line_count += 1
                words = line.split()
                word_count += len(words)
                counter.update(words)
                
                if len(line) > len(longest_line):
                    longest_line = line.rstrip()
        return line_count, word_count, longest_line, counter
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    start = time.perf_counter()
    
    parser = ArgumentParser(description="Simple text analysis tool")

    parser.add_argument("file", help="Path to the file")
    parser.add_argument("--count", action="store_true", help="Count lines and words")
    parser.add_argument("--longest", action="store_true", help="Find the longest line")
    parser.add_argument("--top", type=int, help="Show top N most common words")

    args = parser.parse_args()



    file_path = args.file

    

    if not (args.count or args.longest or args.top):
        try:
            with open(file_path, encoding='utf-8') as file:
                for line in file:
                    print(line.rstrip())
        except FileNotFoundError:
            print(f"File not found.")
        except PermissionError:
            print(f"Permission denied.")
        except UnicodeDecodeError:
            print(f"Could not decode the file at {file_path}. Please ensure it's a text file.") 
    else:
        result = text_tool(file_path)
        if result is None:
            sys.exit(1)
        lines, words, longest, counter = result
        if args.count:
            print(f"Lines: {lines}, Words: {words}")
        elif args.longest:
            print(f"Longest line: {longest}")
        else:
            print(f"Top words: {counter.most_common(args.top)}")

    print(f"Execution time: {time.perf_counter() - start:.3f} seconds")