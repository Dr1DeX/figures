from detector_figures import detector


def main():
    lines = list(map(int, input().split()))
    print(detector(len(lines), lines))


if __name__ == '__main__':
    main()
