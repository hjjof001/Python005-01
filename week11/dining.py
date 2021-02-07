import threading
import queue
import time
import random


class DiningPhilosophers(threading.Thread):
    def __init__(self, philosopher, left_fork, right_fork, count, action_queue):
        super().__init__()
        self.philosopher = philosopher  # 哲学家的编号
        self.leftFork = left_fork
        self.rightFork = right_fork
        self.actionQueue = action_queue
        self.count = count

    def pickLeftFork(self):
        self.actionQueue.put([self.philosopher, 1, 1])

    def pickRightFork(self):
        self.actionQueue.put([self.philosopher, 2, 1])

    def eat(self):
        self.actionQueue.put([self.philosopher, 0, 3])
        time.sleep(0.1 * random.choice([1, 2, 3, 4]))
        self.count -= 1

    def putLeftFork(self):
        self.actionQueue.put([self.philosopher, 1, 2])

    def putRightFork(self):
        self.actionQueue.put([self.philosopher, 2, 2])

    def run(self):
        while True:
            leftpick = self.leftFork.acquire(blocking=False)
            rightpick = self.rightFork.acquire(blocking=False)
            if leftpick and rightpick:
                self.pickLeftFork()
                self.pickRightFork()
                self.eat()
                self.putLeftFork()
                self.putRightFork()
                self.leftFork.release()
                self.rightFork.release()
            elif leftpick and not rightpick:
                self.leftFork.release()
            elif rightpick and not leftpick:
                self.rightFork.release()
            else:
                time.sleep(0.1 * random.choice([1, 2, 3, 4]))
            if self.count < 1:
                break


if __name__ == "__main__":
    n = 1

    fork1 = threading.Lock()
    fork2 = threading.Lock()
    fork3 = threading.Lock()
    fork4 = threading.Lock()
    fork5 = threading.Lock()

    actionQueue = queue.Queue()

    diningPhilosophers1 = DiningPhilosophers(1, fork1, fork2, n, actionQueue)
    diningPhilosophers2 = DiningPhilosophers(2, fork2, fork3, n, actionQueue)
    diningPhilosophers3 = DiningPhilosophers(3, fork3, fork4, n, actionQueue)
    diningPhilosophers4 = DiningPhilosophers(4, fork4, fork5, n, actionQueue)
    diningPhilosophers5 = DiningPhilosophers(5, fork5, fork1, n, actionQueue)

    diningPhilosophers1.start()
    diningPhilosophers2.start()
    diningPhilosophers3.start()
    diningPhilosophers4.start()
    diningPhilosophers5.start()

    diningPhilosophers1.join()
    diningPhilosophers2.join()
    diningPhilosophers3.join()
    diningPhilosophers4.join()
    diningPhilosophers5.join()

    while not actionQueue.empty():
        print(actionQueue.get())