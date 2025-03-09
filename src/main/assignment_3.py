def f(t, y):
    return t - y**2

def euler(f, t0, y0, T, n):
    h = (T - t0) / n
    t, y = t0, y0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y

def rk(f, t0, y0, T, n):
    h = (T - t0) / n
    t, y = t0, y0
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h/2, y + h * k1/2)
        k3 = f(t + h/2, y + h * k2/2)
        k4 = f(t + h, y + h * k3)
        y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
    return y

if __name__ == '__main__':
    print(euler(f, 0, 1, 2, 10))
    print(rk(f, 0, 1, 2, 10))
