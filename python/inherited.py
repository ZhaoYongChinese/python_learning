"""
class 类名(类名):
    继承
"""

class Phone():
    num = None
    processor = None

    def show(self):
        print(f'num = {self.num}, proceder = {self.processor}')

class Phone_v1(Phone):
    face_id = True

    def introduce(self):
        print(self.num, self.face_id)

Phone_1 = Phone()
Phone_1.show()
Phone_2 = Phone_v1()
Phone_2.show()
Phone_2.introduce()