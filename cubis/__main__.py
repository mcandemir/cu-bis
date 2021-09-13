from src.cubis import main
import time

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    print("<*> Executed in {} seconds".format(end-start))
