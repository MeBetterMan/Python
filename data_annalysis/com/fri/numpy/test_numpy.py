# encoding=utf-8
import numpy as np
import matplotlib.pyplot as pt


def main():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)
    pt.figure(1)
    pt.plot(x, c)
    pt.plot(x, s)
    pt.show()


if __name__ == '__main__':
    main()
