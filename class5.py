class sanjay:
    num1=3
    def home(self,a,b):
        self.a=a
        self.b=b
        print("hello world",self.a+self.b)
class mrssanjay:
      num2=5
      def jew(self,a):
          self.a=2000
          print("hi",self.a)
class son1(sanjay,mrssanjay):
      def add(self):
          print(self.num1+self.num2)
obj = son1()
obj.add()
obj.jew(1000)
obj.home(100000,200000)
