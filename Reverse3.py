class Solution:
    def reverse(self, x: int) -> int:
        num = str(abs(x))[::-1]
        
        if (int(num) > ((-2)**31) & int(num) > (((2)**31) - 1)):
            num = '0'
        elif x<0:
            num = '-'+num
        
        print int(num)
        