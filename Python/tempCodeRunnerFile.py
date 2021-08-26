      count += 1
        if count % 5 == 0:
            print("Posed measured")
            print(PRmeasured)
            print("Translation Reference: ", TRref)
            print("Translation Input Delta: ", TRdelta)
            print("Translation Output Delta: ", ORdelta)
            print("Output Reference")
            print(ORref)
            print("Output Pose")
            print(PRreconstruct)

        pyplot.step()