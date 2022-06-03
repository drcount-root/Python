# If a, b and c are three sides of a triangle. Then,
# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

a = float(input("\nEnter side a : "));
b = float(input("\nEnter side b : "));
c = float(input("\nEnter side c : "));

s = (a + b + c)/2;

area = (s * (s-a) * (s-b) * (s-c)) ** (1/2);

print('\nThe area of the triangle having sides of {0:0.1f}, {1:0.1f} & {2:0.1f} is = {3: 0.2f}'.format(a, b, c, area)+'\n');