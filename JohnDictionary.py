
def main():

    outfile = open('book of John text.txt', 'r')

    words = outfile.read().split()

    John = {}

    for w in range(len(words)):
        John[words[w]] = 0

    for w in range(len(words)):
        John[words[w]] += 1

    print("Father: ", John['Father'])
    print("God: ", John['God'])
    print("Christ: ", John['Christ'])
    print("Spirit: ", John['Spirit'])
    print("spirit: ", John['spirit'])
    print("life: ", John['life'])
    print("man: ", John['man'])

    outfile.close()

main()
