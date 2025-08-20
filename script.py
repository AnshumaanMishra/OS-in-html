for i in range(1000):
    f = open(f"a{i}.html", "w")
    f.write(f"{i}th part of OS is done")
    f.close()
