
def ft_tqdm(lst: range) -> None:
    length = len(lst)

    def print_bar(i: int, length: int):
        percent = int(i * 100 / length)
        filled = int(50 * i / length)
        empty = 50 - filled
        print('\r', end='')
        print(f'{percent:3}%|{"█" * filled}{" " * empty}|', end='')
        print("{i:{length}}".format(i=i, length=len(str(length))), end='')
        print(f'/{length}', end='', flush=True)

    for i in lst:
        if i % 20 == 0:
            print_bar(i, length)
        yield i
    print_bar(length, length)

