def process_file():
    try:
        f=open("F:\\Python\\working with json\\data\\funny.txt")
        x=1/0
    except FileNotFoundError as e:
        print("Inside except")
    finally:
        print("cleaning up files")
        f.close()

process_file()