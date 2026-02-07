
import sys
import time

#this is to calculate how much it takes to analize the file

start = time.perf_counter()
#here "file_path" doesnt have a value yet so we will assign it now
file_path = sys.argv[1]
file = open(file_path, 'r')


def read_file(file_path):
    try:
        for line in file:
            print(line.strip())
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except PermissionError:
        print(f"Permission denied for file at {file_path}.")
    except IOError:
        print(f"An I/O error occurred while accessing the file at {file_path}.")
    except UnicodeDecodeError:
        print(f"Could not decode the file at {file_path}. Please ensure it's a text file.") 
    except Exception as e:
        print(f"An error occurred: {e}")

#this will count the amount of lines and word in a file.

def count_line_and_words(file_path):
    try:
        lines = file.readlines()
        line_count = len(lines)
        # count words by splitting each line (file is already read into `lines`)
        word_count = sum(len(line.split()) for line in lines)
        print(f"Lines: {line_count}, Words: {word_count}")
        #here we use "line.split()" to split each line into words and count them.
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except PermissionError:
        print(f"Permission denied for file at {file_path}.")
    except IOError:
        print(f"An I/O error occurred while accessing the file at {file_path}.")   
    except UnicodeDecodeError:
        print(f"Could not decode the file at {file_path}. Please ensure it's a text file.") 
    except ValueError:
        print(f"Invalid value encountered while processing the file at {file_path}.")
    except TypeError:
        print(f"Type error occurred while processing the file at {file_path}.")
    except KeyError:
        print(f"Key error occurred while processing the file at {file_path}.")
    except IndexError:
        print(f"Index error occurred while processing the file at {file_path}.")
    except ZeroDivisionError:
        print(f"Zero division error occurred while processing the file at {file_path}.")
    except MemoryError:
        print(f"Memory error occurred while processing the file at {file_path}.")
    except OverflowError:
        print(f"Overflow error occurred while processing the file at {file_path}.")
    except RecursionError:
        print(f"Recursion error occurred while processing the file at {file_path}.")
    except ImportError:
        print(f"Import error occurred while processing the file at {file_path}.")
    except ModuleNotFoundError:
        print(f"Module not found error occurred while processing the file at {file_path}.") 
    except AttributeError:
        print(f"Attribute error occurred while processing the file at {file_path}.")
    except StopIteration:
        print(f"Stop iteration error occurred while processing the file at {file_path}.")
    except KeyboardInterrupt:
        print(f"Process was interrupted while processing the file at {file_path}.")
    except SystemExit:
        print(f"System exit occurred while processing the file at {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
        #here "e" is the variable that holds the error message.

#this will find the longest line in the file.

def find_longest_line(file_path):
    try:
        longest_line = ""
        for line in file:
            if len(line) > len(longest_line):
                longest_line = line
        print(f"Longest line: {longest_line.strip()}")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#this will list the top words in the file.

def top_words(file_path, top_n):
    
    from collections import Counter
    try:
        top_n = sys.argv[3]
        top_n = int(top_n)
        print(f"top_n: {top_n}")
        text = file.read()
        words = text.split()
        words_count = Counter(words)
        most_common = words_count.most_common(top_n)
        print(f"Top {top_n} words: {most_common}")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except ValueError:
        print(f"Invalid value for top_n: {top_n}. Please provide an number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file_path> [action]")
        print("Actions: read (default), count, longest, top")
        sys.exit(1)

    file_path = sys.argv[1]
    action = sys.argv[2] if len(sys.argv) > 2 else "read"

    if action == "read":
        read_file(file_path)
    elif action == "count":
        count_line_and_words(file_path)
    elif action == "longest":
        find_longest_line(file_path)
    elif action == "top":
        top_words(file_path, top_n=5)
    else:
        print(f"Unknown action: {action}")


print(f"Execution time: {time.perf_counter() - start:.3f} seconds")