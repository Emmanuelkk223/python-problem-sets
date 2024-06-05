def main():
    file_name = input("File name: ")
    file_name = m(file_name)
    print(file_name)

def m(n):
    if n.endswith(".gif"):
        return "image/gif"
    elif n.endswith(".jpg") or n.endswith(".jpeg"):
        return "image/jpeg"
    else:
        return "application/octet-stream"
if __name__ == '__main__':
    main()
