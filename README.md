# Pwned Passwords Range Downloader
This script allows you to download hash ranges of compromised passwords from the Pwned Passwords API concurrently. It can help you build a local copy of the Pwned Passwords database for offline use.

## Usage
### Prerequisites
* Python 3.x
* Dependencies can be installed using `pip install requests tqdm`

### Running the Script

```bash
python script_name.py output_file [-t NUM_THREADS]
```
* `output_file`: Path to the output file where hash ranges will be saved.
* `-t` NUM_THREADS: (Optional) Number of threads to use (default is 16).

### Example
```bash
python haveibeenpwned-download.py pawned.txt -t=16
```
### Important Notes
* Ensure you have a stable internet connection before running the script.
* Adjust the number of threads (-t) to match your system's capabilities and internet speed for optimal performance.
