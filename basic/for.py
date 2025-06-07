import unittest


def case_for():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

    users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    print(len(users))
    for user, status in users.copy().items():
        if status == 'active':
            del users[user]
    print(len(users))

    return True


def case_range():
    for i in range(5):
        print('i=', i)

    for i in range(5, 10):
        print(i)

    print(list(range(0, 20, 3)))
    print(list(range(-10, -100, -20)))

    return False


def case_else():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n/x)
            else:
                print(n, 'is a prime number')
    return False


class TestFor(unittest.TestCase):
    def test_cases(self):
        # self.assertTrue(case_for())
        # self.assertFalse(case_range())
        self.assertFalse(case_else())


if __name__ == '__main__':
    unittest.main()
