import sys
import math


if len(sys.argv) != 4:
    print("<h3>Error: Invalid number of arguments.</h3>")
    sys.exit(1)

try:  
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
except ValueError:
    print("<h3>Error: All inputs must be numeric.</h3>")
    sys.exit(1)

if a < 1:
    print("<h3>The value of a is too small </h3>" )
if b == 0:
    print("<h3>The value of b will not affect the result </h3>")
if c < 0:
    print("<h3> C can not be negative </h3>")

c_cubed = c ** 3
result = math.sqrt(c_cubed)  

if c_cubed > 1000:
    result *= 10
else:
    if a != 0: 
        result /= a

final_result = result + b

print(f"""
<h3>Calculation Results:</h3>
<ul>
    <li>c³ = {c_cubed}</li>
    <li>Square root of c³ = {math.sqrt(c_cubed)}</li>
    <li>Final result = {final_result}</li>
</ul>
""")



# ori_x = x

# x += y 
# s1 = x

# x -= z  
# s2 = x

# x *= y  
# s3 = x

# x %= z  
# s4 = x

# if z != 0:
#     x /= z  
# else:
#     x = "undefined"  


# if isinstance(x, (int, float)):
#     final_result = ori_x + y + z + s1 + s2 + s3 + s4 + x
# else:
#     final_result = "Cannot divide by zero."


# print(f"<h3> Original Values:</h3>")
# print(f"<ul>")
# print(f"<li> x: {ori_x}")
# print(f"</li>")
# print(f"<li> y: {y}</li>")
# print(f"<li> z: {z}</li>")
# print(f"</ul>")

# print(f"<h3> Calculation Steps:</h3>")
# print(f"<ol>")
# print(f"<li> Initial Value of x: {ori_x}</li>")
# print(f"<li> After x += y: {s1}</li>")
# print(f"<li> After x -= z: {s2}</li>")
# print(f"<li> After x *= y: {s3}</li>")
# print(f"<li> After x %= z: {s4}</li>")
# print(f"<li> After x /= z: {x}</li>")
# print(f"</ol>")
# print(f"<h3> Final Result: {final_result}</h3>")

