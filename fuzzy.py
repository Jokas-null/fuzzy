import sys

##if len(sys.argv) != 2:
 #   print("\n[*] Usage: python3 " + sys.argv[0] + " <path_file>")
 #   sys.exit(1)

#file = sys.argv[1]

f = open("10k-most-common.txt", "r")

for data in f.readlines():
    data = data.strip()

    print("La ruta es: ", data)