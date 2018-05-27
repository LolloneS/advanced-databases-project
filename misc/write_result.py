def write_result(s, mode="a"):
    results = open("results.txt", mode)
    results.write(s + "\n")
    results.close()
