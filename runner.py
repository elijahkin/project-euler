import time, os

# Run solution to specified problem and time how long it takes
def run(problem):
    t = time.time()
    os.system('python3 {}.py'.format(problem))
    print('Found answer in {} seconds'.format(time.time()-t))

run('100')