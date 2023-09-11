# Mutation-based Fuzzer in Python

## Overview
This Python script performs mutation-based fuzzing on JPEG files to identify bugs in a target program. The script uses Python's subprocess and regular expressions to run the target executable (jpeg2bmp) and parse its output, respectively.

## Requirements
- Python 3.x
- jpeg2bmp executable in the same directory

## Features
- Reads a sample JPEG file ('cross.jpg') into a byte array.
- Randomly mutates a byte at a random index in the byte array.
- Writes the mutated byte array to a new JPEG file ('test.jpg').
- Runs jpeg2bmp executable to test the mutated JPEG file.
- Parses the standard error output to identify any triggering bugs.
- Keeps a count of how many times each identified bug is triggered.
- Renames the JPEG file to include the triggered bug number for further analysis.

## Usage
Simply run the script in the directory where both the script and jpeg2bmp executable are located:
```Python
python fuzzingTest.py
```

## Output
The script will output the count of how many times each identified bug is triggered, e.g.,
```
Bug 1 is encountered 5 times
Bug 2 is encountered 3 times
...
```

## Limitations
- The script assumes that jpeg2bmp outputs bug information in a specific format.
- The fuzzer is relatively basic and operates on random mutations; it doesn't employ any advanced fuzzing techniques.
- Hardcoded to only run for 100 iterations, which could be modified as per your requirements.

## Customization
To use different input files or change the number of iterations, modify the appropriate variables in the code.

## Caution
Ensure you have the right permissions and environment to run this script as it may trigger bugs that could potentially cause issues.

## License
This script is intended for ethical and legal usage only. Unauthorized use is strictly prohibited.


