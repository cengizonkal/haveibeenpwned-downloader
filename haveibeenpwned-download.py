import argparse
import requests
from tqdm import tqdm


def download_range(session, current_hash):
    url = f"https://api.pwnedpasswords.com/range/{get_hash_range(current_hash)}"
    response = session.get(url)
    content = response.text
    return content


def main(output_file_path):
    client = requests.Session()
    output_file = open(output_file_path, "w")
    pbar = tqdm(total=1024 * 1024, desc="Downloading")
    for current_hash in range(1024 * 1024):
        result = download_range(client, current_hash)
        pbar.update(1)
        output_file.writelines(result)
    print(f"Downloaded and saved all hash ranges to {output_file_path}")


def get_hash_range(i):
    return f"{i:05X}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    main(args.output_file)
