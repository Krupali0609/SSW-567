""" The program classifies the different triangles  """
import random

def classifyTriangle(a:float,b:float,c:float):
    if a>0 and b>0 and c>0:                                        # No zero value for any side
        if a + b > c or b + c > a or c + a > b  :                  # Triangle condition should be true
            if  a!= b and  b !=c  and  c!= a:                      # Condition For Scalene Triangle
                if a*a  +  b*b == c*c:                             # Condition For Right Triangle
                    return "The triangle is Scalene as well as a Right"
                else:
                    return "The Triangle is Scalene"
            elif a == b == c:                                      # Condition For Equilateral Triangle
                return "The Triangle is an Equilateral"

            elif  a == b or  b == c  or  c == a:
                if a*a  +  b*b == c*c:                             # Condition For Right Triangle
                    return "The triangle is Isosceles as well as a Right"
                else:
                    return "The Triangle is Isosceles"
        else:
            print("The sides are cannotform the triangle: Invalid input")
    else:
        return "The side cannot be 0"

 
    
def main()-> None:
    string:str = "Enter the the length of the sides of Triangle"
    """the below print is to skip a line foR better presentation"""
    print("\n")
    """"Just to repesent centered the string in output"""
    centered_string =string.center(100,'-') 
    print(centered_string )
    a=float(input("Enter the length of the side 1:"))
    b=float(input("Enter the length of the side 2:"))
    c=float(input("Enter the length of the side 3:"))
    print(f"{a} {b} {c}")
    print(classifyTriangle(a,b,c))


#excution starts from here
if __name__ == '__main__':        
    main()


