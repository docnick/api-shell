import multiprocessing
import requests
import datetime
import sys

TEST_API_URL = "http://localhost:5000/test"

lock = multiprocessing.Lock()


def output(msg):
    msg = '{}\n'.format(msg)
    with lock:
        sys.stdout.write(msg)


def make_request(param):
    call_time = datetime.datetime.now()
    req = requests.get('{}?param={}'.format(TEST_API_URL, param))
    now = datetime.datetime.now()

    output('NOW: {}\n\tCall time: {}\n\t{}'.format(now, call_time, req.text))


def test_concurrent_calls(n):
    params = range(n)
    p = multiprocessing.Pool(n)
    print('Testing...')
    p.map(make_request, params)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print('{} concurrent calls...'.format(n))

    test_concurrent_calls(n)