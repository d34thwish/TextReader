# Text Reader

Simple command-line text analysis tool written in Python.

## Features

- Print file contents
- Count lines and words
- Find the longest line
- Show the most frequent words in the file

## Requirements

Python 3.x

## Usage

Run the program with a text file path and optional flags.

Print file contents (default):

```bash
python main.py text.txt
```

Count lines and words:

```bash
python main.py text.txt --count
```

Find the longest line:

```bash
python main.py text.txt --longest
```

Show top N most common words:

```bash
python main.py text.txt --top 5
```

## Example Output

```
$ python main.py text.txt --count
Lines: 3, Words: 9
Execution time: 0.002 seconds
$ python main.py text.txt --top 3
Top words: [('the', 4), ('text', 2), ('example', 2)]
Execution time: 0.002 seconds
```

## Project Structure

- `main.py` – main script for text analysis
- `text.txt` – sample input file
- `text2.txt` – additional sample file

## Learning Notes

This project was built as a learning exercise to practice:

- Python file handling
- command line argument parsing (`argparse`)
- word frequency analysis (`collections.Counter`)

Some guidance was used during development as part of the learning process.  
All code in this repository has been reviewed and understood by the author.

## License

MIT License

## Contact

Ade - ademirsteventm@gmail.com
