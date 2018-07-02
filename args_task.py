import argparse


def string_sum(string):
    digits = [int(char) for char in string if char.isdigit()]
    return sum(digits)


def ladder(string):
    n_steps = int(string) if string.isdigit() else 1
    result = ''
    for i in range(1, n_steps+1):
        step = '#'*i
        result += f'{step:{n_steps}}'[::-1] + '\n'
    return result


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', '--task', help='Type of task', type=int)
    parser.add_argument('-v', '--value', help='Task argument value')

    args = parser.parse_args()

    try:
        tasks = {
            1: string_sum,
            2: ladder
        }
        print(tasks[args.task](args.value))

    except KeyError as e:
        print('Task type error, check your input and try again.')


if __name__ == '__main__':
    main()
