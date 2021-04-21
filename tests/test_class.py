class TestClass:
    def test_one(self):
        name = 'Sachin Vijay'
        assert 'Sa' in name

    def test_two(self):
        x = "hello"
        assert hasattr(x,"check")