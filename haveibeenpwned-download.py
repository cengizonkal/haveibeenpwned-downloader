import argparse
import requests
from tqdm import tqdm
import concurrent.futures

NUM_THREADS = 16  # You can adjust the number of threads as needed


def download_range(session, current_hash):
    url = f"https://api.pwnedpasswords.com/range/{get_hash_range(current_hash)}"
    response = session.get(url)
    content = response.text
    return content


def download_ranges_concurrently(output_file_path, num_threads=NUM_THREADS):
    client = requests.Session()
    with open(output_file_path, "w") as output_file:
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            pbar = tqdm(total=1024 * 1024, desc="Downloading")

            for current_hash in range(1024 * 1024):
                future = executor.submit(download_range, client, current_hash)
                future.add_done_callback(lambda f: futures.remove(f))  # Remove completed future
                futures.append(future)

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                output_file.write(result)
                pbar.update(1)
            pbar.close()

    print(f"Downloaded and saved all hash ranges to {output_file_path}")


def get_hash_range(i):
    return f"{i:05X}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("-t", help="Number of threads to use", type=int, default=NUM_THREADS)
    args = parser.parse_args()

    download_ranges_concurrently(args.output_file, args.t)
