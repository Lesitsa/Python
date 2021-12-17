import password_TDD_2

class Test_password:

    def test_password_qwert(self):
        assert password_TDD_2.check('qwert') == False
    
    def test_password_1234567(self):
        assert password_TDD_2.check('1234567') == False

    def test_password_qwerty(self):
        assert password_TDD_2.check('qwerty') == False
    
    def test_password_PassWord007(self):
        assert password_TDD_2.check('PassWord007') == False
    
    def test_password_pasWord7(self):
        assert password_TDD_2.check('pasWord7') == True
    
    def test_password_qwerty007(self):
        assert password_TDD_2.check('qwerty007') == True
    