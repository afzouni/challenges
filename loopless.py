def loopless(counter = 1):
    if counter <= 100:
        print(counter)
        loopless(counter + 1)

loopless()