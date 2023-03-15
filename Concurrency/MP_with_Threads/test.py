import multiprocessing

class mProcessing_using_Pool:
    def __init__(self,parm ,print_square ,arguments):
        self.parm = parm
        self.print_square = print_square
        self.arguments = arguments


    def run(self):
        set_size = len(self.arguments)//self.parm
        pool = multiprocessing.Pool(processes=set_size)
        for i in (pool.map(print_square, self.arguments)):
            print(i)
        

def print_square(num):
    return num**2


if __name__ == "__main__":
    list = [2,3,4,9,5,10,8,7,11]
    parm = 4
    mp = mProcessing_using_Pool(parm, print_square, list)
    mp.run()