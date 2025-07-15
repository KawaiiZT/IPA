def test_fizzbuz():
    assert 1 == fizzbuzz(1)
    assert 2 == fizzbuzz(2)
    assert "Fizz" == fizzbuzz(3)
    assert 4 == fizzbuzz(4)
    assert "Buzz" == fizzbuzz(5)
    assert "Fizz" == fizzbuzz(6)
    assert 7 == fizzbuzz(7)
    assert 8 == fizzbuzz(8)
    assert "Fizz" == fizzbuzz(9)
    assert "Buzz" == fizzbuzz(10)
    assert 11 == fizzbuzz(11)
    assert "Fizz" == fizzbuzz(12)
    assert 13 == fizzbuzz(13)
    assert 14 == fizzbuzz(14)
    assert "FizzBuzz" == fizzbuzz(15)
    assert "FizzBuzz" == fizzbuzz(30)
    print ("All Test case Pass")
def test_true():
    assert False
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
test_fizzbuz()

