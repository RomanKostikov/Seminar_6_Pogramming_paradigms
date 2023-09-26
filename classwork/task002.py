import random


def mse(arr1, arr2):
    sum_diff_x_y = sum(map(lambda x, y: (x - y) ** 2, arr1, arr2))

    return round(sum_diff_x_y / len(arr1), 2)


def main():
    array_x, array_y = [], []

    for i in range(7):
        array_x.append(random.randint(0, 10))
        array_y.append(random.randint(0, 10))
        print(f'Array of X: {array_x} \nArray of Y: {array_y}')
        print(f'\nMSE = {mse(array_x, array_y)}')


if __name__ == "__main__":
    main()
