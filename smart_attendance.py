# 1. Attendance lagane ka function
def mark_attendance(students, record):
    print("\n--- Attendance Start ---")
    for student in students:
        status = input(f"{student} is present ? (P/A): ").strip().upper()
        
        # 'P' dabaya toh Present, warna (default) Absent
        if status == 'P':
            record[student] = "Present"
        else:
            record[student] = "Absent"
            
    print("Attendance was done \n")





# 2. Sabki list dekhne ka function
def view_report(record):
    print("\n--- Full Report ---")
    if not record: # Agar dictionary khali hai
        print("Please mark your attendance first (Option 1).")
        return
        
    for student, status in record.items():
        print(f"{student}: {status}")





# 3. Sirf chhutti (Absent) walo ki list
def show_absent(record):
    print("\n--- Absent Students ---")
    if not record:
        print("Please mark your attendance first (Option 1).")
        return
        
    absent_students = [student for student, status in record.items() if status == "Absent"]
    
    if not absent_students:
        print("Wow Everyone in class is here today..")
    else:
        for student in absent_students:
            print(f" {student}")
        print(f"Total Absent: {len(absent_students)}")





# 4. Main Menu System
def start_system():
    students = [
    "Ratnesh Kesarwani", "Mohammad Sanif", "Mohammad Unaish", "Mugdha", "Naitik Agrahari",
    "Nishant Maurya", "Om Mishra", "Pankaj Kumar Yadav", "Prashant Raj", "Pratyaksh Kumar",
    "Prince Pandey", "Priyanshu Pandey", "Priyanshu Upadhyay", "Pushpendra Yadav", "Raj Sahu",
    "Rishabh", "Rishabh Pandey", "Rishal Singh Yadav", "Ritesh Agrahari", "Riya Singh",
    "Rudra Pratap Singh", "Sachin Tiwari", "Sakshi Devi", "Samriddhi Vaish", "Sandeep Kumar",
    "Sanskriti Jaiswal", "Sanya Singh", "Sarthak Srivastava", "Sarthak Srivastava", "Sarthak Yadav",
    "Saurabh Yadav", "Shashank Mishra", "Shivam Maurya", "Shivam Patel", "Shivanshu Sharma",
    "Shobhit Singh", "Shraddha Tiwari", "Shreya Maurya", "Siddhi Keshari", "Simran Rawat",
    "Sufiyan Akhtar", "Sumit Shukla", "Sumit Yadav", "Sushipra Tripathi", "Swati Sagar Singh",
    "Swayam Khare", "Swikriti Prakash", "Tafseer Alam", "Tamish Ruyyan", "Tanisha Jaiswal",
    "Tanishka Yadav", "Tannu Kumari", "Tanu Pushpakar", "Tanu Yadav", "Ujjawal Singh",
    "Utkarsh", "Utkarsh Yadav", "Utkarsh Yadav", "Vaibhav Agarwal", "Vaibhav Laxmi Pandey",
    "Vidyesh Tripathi", "Vinay Shukla", "Yash Dhir", "Yash Dubey", "Yugank Raj Yadav",
    "Yuvraj Singh", "Yuvraj Singh"
]

    record = {} # Attendance ka data yahan save hoga
    
    print("Welcome to Unitde University Smart Attendance System")
    
    while True:
        print("\n=== BCA IBM MENU ===")
        print("1. Mark Attendance")
        print("2. View Full Report")
        print("3. Show Absent Students")
        print("4. Exit")
        
        choice = input("Choose an Option (1/2/3/4): ")
        
        if choice == '1':
            mark_attendance(students, record)
        elif choice == '2':
            view_report(record)
        elif choice == '3':
            show_absent(record)
        elif choice == '4':
            print("The system is shutting down. Bye...")
            break
        else:
            print(" Invalid input. Please press 1, 2, 3, or 4.")

# Program ko run karne ke liye
start_system()
