from sys import argv


def get_int(prompt):
    while True:
       try:
          return int(input(prompt))
       except ValueError as e:
          print(f"{e}")


def add(a, b):
    return a + b


def div(a, b):
    return a / b


def main():
    x = get_int("what's x: ")
    y = get_int("what's y: ")

    if len(argv) == 2:
      if argv[1] == 'a':
        z = add(x, y)
      elif argv[1] == 'b':
        z = div(x, y)
    else:
        print('missing argument')
    try:
       print(z)
    except UnboundLocalError as e:
       print('incnow argument')


if __name__ == "__main__":
    main()
