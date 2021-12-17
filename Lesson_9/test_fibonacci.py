import fibonacci_1

class Test_Fibonacci_number:

    def test_fibonacci_3(self):
        assert fibonacci_1.fibonacci(3) == 1
    
    def test_fibonacci_27(self):
        assert fibonacci_1.fibonacci(27) == 121393

    def test_fibonacci_60(self):
        assert fibonacci_1.fibonacci(60) == 956722026041

    def test_fibonacci_100(self):
        assert fibonacci_1.fibonacci(100) == 218922995834555169026
    
    def test_fibonacci_0(self):
        assert fibonacci_1.fibonacci(0) == 'Номер не может быть отрицательным или равным 0!'
