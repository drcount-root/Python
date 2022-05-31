# For positive numbers

num = float(input("Enter the num : "));

num_sqrt = num ** (1/2);

print("The square-root of %0.1f is %0.1f" %(num, num_sqrt));

print("The square-root of {0} is {1}".format(num, num_sqrt));


# For real or complex numbers

import cmath;

num_adv = eval(input("Enter the num_adv : "));

num_sqrt_adv = cmath.sqrt(num_adv);
print("The square-root of {0} is {1: 0.2f}+{2: 0.2f}i" .format(num_adv, num_sqrt_adv.real, num_sqrt_adv.imag));