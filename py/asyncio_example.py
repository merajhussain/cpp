import asyncio
import time


async def fetch(name,delay):
    print("Starting {}".format(name))
    await asyncio.sleep(delay)
    print("Finished {}".format(name))

async def sequential():
    await fetch("A", 3)
    await fetch("B", 2)

async def concurrent():
    await asyncio.gather(
        fetch("A", 3),
        fetch("B", 2)
    )


async def main():
    print("=== Sequential ===")
    start = time.perf_counter()
    await sequential()
    seq_time = time.perf_counter() - start
    print(f"Sequential total: {seq_time:.2f}s")

    print("\n=== Gather ===")
    start = time.perf_counter()
    await concurrent()
    gat_time = time.perf_counter() - start
    print(f"Gather total:     {gat_time:.2f}s")

    print(f"\nSpeedup: {seq_time / gat_time:.1f}x faster with gather")

asyncio.run(main())


