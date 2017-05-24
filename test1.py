import test
import rk4

y = rk4.rk4(test.f,11,0.0,0.1,1.0)
print y
