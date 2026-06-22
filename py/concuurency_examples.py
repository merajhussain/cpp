import time
from concurrent.futures import ThreadPoolExecutor


def downloader(url):
    time.sleep(2)#replace with actual download logic
    return "{} download completed".format(url)


def main(urls):
    """
    Create a thread pool and download specified urls
    """
    with ThreadPoolExecutor(max_workers=5) as executor:
        return executor.map(downloader, urls, timeout=60)

if __name__ == '__main__':
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    results = main(urls)
    for result in results:
        print(result)