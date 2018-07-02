import argparse
import os
import tempfile
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

is_storage_exist = False


def init_storage():
    with open(storage_path, 'w') as f:
        f.write(json.dumps({'test': 'test'}))


def read(key=''):
    with open(storage_path, 'r') as f:
        storage_data = f.read()
        jsonify = json.loads(storage_data)
        try:
            return jsonify if len(key) == 0 else jsonify[key]
        except KeyError as e:
            print(f'Something wrong, key doesn\'t exist!\n{e}')
            return None


def write(key, value):
    with open(storage_path, 'w') as f:

        storage_data = read()

        if key not in storage_data:
            storage_data[key] = value
            f.write(json.dumps(storage_data))
            return True
        else:
            return False


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-k', '--key', help='Storage key value')
    parser.add_argument('-v', '--value', help='Storage value for saving')

    args = parser.parse_args()

    if args.key is not None:
        if args.value is not None:
            write(str(args.key), str(args.value))
        else:
            print(read(args.key))
    else:
        print('Try to use --key[-k]/--value[-v] attributes')


if __name__ == '__main__':
    main()
