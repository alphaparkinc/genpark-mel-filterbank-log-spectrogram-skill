from client import MelFilterbank

def main():
    print("=== Testing Mel Filterbank Analyzer ===")
    mfb = MelFilterbank()
    filters = mfb.compute_filterbank(num_filters=4, n_fft=16, sample_rate=8000)

    print(f"Generated {len(filters)} Mel triangular filter vectors:")
    for idx, f in enumerate(filters):
        print(f"  Channel {idx}: {[round(x, 2) for x in f]}")

    assert len(filters) == 4
    assert len(filters[0]) == 9
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
