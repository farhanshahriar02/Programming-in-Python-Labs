marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
    print("Grade Point: 4.00")
elif marks >= 85:
    print("Grade: A-")
    print("Grade Point: 3.70")
elif marks >= 80:
    print("Grade: B+")
    print("Grade Point: 3.30")
elif marks >= 75:
    print("Grade: B")
    print("Grade Point: 3.00")
elif marks >= 70:
    print("Grade: B-")
    print("Grade Point: 2.70")
elif marks >= 65:
    print("Grade: C+")
    print("Grade Point: 2.30")
elif marks >= 60:
    print("Grade: C")
    print("Grade Point: 2.00")
elif marks >= 50:
    print("Grade: D")
    print("Grade Point: 1.00")
else:
    print("Grade: F")
    print("Grade Point: 0.00")