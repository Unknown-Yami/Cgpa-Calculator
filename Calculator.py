# Name: Oluwarotimi Agunloye David Funso 
# Matric No: 25/17788

def get_grade_and_points(score):
    if score >= 70:
        return 'A', 5
    elif score >= 60:
        return 'B', 4
    elif score >= 50:
        return 'C', 3
    elif score >= 45:
        return 'D', 2
    elif score >= 40:
        return 'E', 1
    else:
        return 'F', 0

def calculate_cgpa():
    print("="*40)
    print("  CGPA CALCULATOR")
    print("="*40)
    
    try:
        num_courses = int(input("Enter the number of courses: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    results = []
    total_units = 0
    total_weighted_points = 0

    for i in range(num_courses):
        print(f"\nCourse {i+1}:")
        name = input("  Course Code/Name: ")
        try:
            unit = int(input(f"  Credit Units: "))
            score = float(input(f"  Score (0-100): "))
            
            grade, points = get_grade_and_points(score)
            weighted_point = unit * points
            
            total_units += unit
            total_weighted_points += weighted_point
            
            results.append([name, unit, score, grade, points])
        except ValueError:
            print("  Invalid data entered.")

    # Display results
    print("\n\n" + " SUMMARY ".center(50, "-"))
    print(f"{'Course':<15} {'Units':<8} {'Score':<8} {'Grade':<8} {'GP':<8}")
    print("-" * 50)
    
    for res in results:
        print(f"{res[0]:<15} {res[1]:<8} {res[2]:<8.1f} {res[3]:<8} {res[4]:<8}")

    print("-" * 50)
    
    if total_units > 0:
        cgpa = total_weighted_points / total_units
        print(f"TOTAL UNITS: {total_units}")
        print(f"TOTAL POINTS: {total_weighted_points}")
        print(f"FINAL CGPA:   {cgpa:.2f}")
        
        # Classification
        if cgpa >= 4.50: class_type = "First Class"
        elif cgpa >= 3.50: class_type = "Second Class Upper"
        elif cgpa >= 2.40: class_type = "Second Class Lower"
        elif cgpa >= 1.50: class_type = "Third Class"
        else: class_type = "Pass/Probation"
        
        print(f"CLASSIFICATION: {class_type}")
    else:
        print("No valid data to calculate CGPA.")
    print("="*50)

if __name__ == "__main__":
    calculate_cgpa()
