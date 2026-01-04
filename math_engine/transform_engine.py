import numpy as np

class TransformEngine:
    def __init__(self, A=None, b=None, c=None, d=1.0):
        self.A = A if A is not None else np.eye(3)
        self.b = b if b is not None else np.zeros((3, 1))
        self.c = c if c is not None else np.zeros((1, 3))
        self.d = d

    def matrix(self):
        top = np.hstack([self.A, self.b])
        bottom = np.hstack([self.c, np.array([[self.d]])])
        return np.vstack([top, bottom])

    def apply(self, point):
        X = np.array([[point[0]], [point[1]], [point[2]], [1.0]])
        Xp = self.matrix() @ X
        w = Xp[3, 0]
        return (Xp[:3, 0] / w).tolist()

    @staticmethod
    def rotation_y(theta):
        A = np.array([
            [ np.cos(theta), 0, np.sin(theta)],
            [0, 1, 0],
            [-np.sin(theta), 0, np.cos(theta)]
        ])
        return TransformEngine(A=A)

    @staticmethod
    def perspective(px, py, pz, d=1.0):
        c = np.array([[px, py, pz]])
        return TransformEngine(c=c, d=d)
