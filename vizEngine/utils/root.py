def dir():
    file = __file__
    
    # use this split when in windows
    split = file.split('\\')

    # use this split when in linux
    # split = file.split('/')

    split.pop()
    path = [i for i in split if i != split[len(split) - 1]]
    path.pop()
    path = '/'.join(i for i in path)
    return path

print(f"Root found at: {dir()}")