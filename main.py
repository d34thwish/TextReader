
import sys
import time

#this is to calculate how much it takes to analize the file

start = time.perf_counter()
#here "file_path" doesnt have a value yet so we will assign it now
file_path = sys.argv[1]
file = open(file_path, 'r')

line_count = 0
word_count = 0


def read_file(file_path):
    try:
        for line in file:
            print(line.strip())
    except FileNotFoundError:
        print(f"The file is not there pal.")
    except PermissionError:
        print(f"Actually, you can't do that.")
    except OSError:
        print(f"An OS error occurred while accessing the file at {file_path}.")
    except UnicodeDecodeError:
        print(f"Could not decode the file at {file_path}. Please ensure it's a text file.") 
    except Exception as e:
        print(f"An error occurred: {e}")

#this will count the amount of lines and word in a file.

def count_line_and_words(file_path):
    try:
        for line in file:
            line_count += 1
            word_count += len(line.split())
        
        print(f"Lines: {line_count}, Words: {word_count}")
        #here we use "line.split()" to split each line into words and count them.
    except FileNotFoundError:
        print(f"The file is not there pal.")
    except PermissionError:
        print(f"Actually, you can't do that.")
    except Exception as e:
        print(f"An error occurred: {e}")

#this will find the longest line in the file.

def find_longest_line(file_path):
    try:
        longest_line = ""
        for line in file:
            if len(line) > len(longest_line):
                longest_line = line
        print(f"Longest line: {longest_line.strip()}")
    except FileNotFoundError:
        print(f"The file is not there pal.")
    except Exception as e:
        print(f"An error occurred: {e}")

#this will list the top words in the file.

def top_words(file_path, top_n):
    
    from collections import Counter
    try:
        print(f"top_n: {top_n}")
        text = file.read()
        words = text.split()
        words_count = Counter(words)
        most_common = words_count.most_common(top_n)
        print(f"Top {top_n} words: {most_common}")
    except FileNotFoundError:
        print(f"The file is not there pal.")
    except ValueError:
        print(f"Invalid value for top_n: {top_n}. Please provide an number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file_path> [action]")
        print("Actions: read (default), count, longest, top")
        sys.exit(1)

    action = sys.argv[2] if len(sys.argv) > 2 else "read"

    if action == "read":
        read_file(file_path)
    elif action == "count":
        count_line_and_words(file_path)
    elif action == "longest":
        find_longest_line(file_path)
    elif action == "top":
        top_n = int(sys.argv[3])
        top_words(file_path, top_n)
    else:
        print(f"Unknown action: {action}")


print(f"Execution time: {time.perf_counter() - start:.3f} seconds")