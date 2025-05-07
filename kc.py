jobs = []
admin_username = None
admin_password = None

def add_job():
    title = input("Enter job title: ")
    company = input("Enter company name: ")
    level = input("Enter job level (e.g., Entry-level, Internship): ")
    location = input("Enter job location (e.g., City, State, or Remote): ")
    salary = input("Enter salary (e.g., $3000/month or $50,000/year): ")
    age_req = input("Enter age requirement (e.g., 21+, None): ")
    needed = int(input("Enter number of applicants needed: "))
    job = {
        "title": title,
        "company": company,
        "level": level,
        "location": location,
        "salary": salary,
        "age_requirement": age_req,
        "applied": False,
        "applicants_needed": needed,
        "applicants": []
    }
    jobs.append(job)
    print("Job added.")

def edit_job():
    title = input("Enter job title to edit: ")
    for job in jobs:
        if job["title"].lower() == title.lower():
            job["title"] = input("Enter new job title: ")
            job["company"] = input("Enter new company name: ")
            job["level"] = input("Enter new job level: ")
            job["location"] = input("Enter new location: ")
            job["salary"] = input("Enter new salary: ")
            job["age_requirement"] = input("Enter new age requirement: ")
            job["applicants_needed"] = int(input("Enter new number of applicants needed: "))
            print("Job updated.")
            return
    print("Job not found.")

def delete_job():
    title = input("Enter job title to delete: ")
    for job in jobs:
        if job["title"].lower() == title.lower():
            jobs.remove(job)
            print("Job deleted.")
            return
    print("Job not found.")

def search_job():
    title = input("Enter job title to search: ")
    for i, job in enumerate(jobs):
        if job["title"].lower() == title.lower():
            applied_status = "Yes" if job["applied"] else "No"
            print(f"Job found at position {i}:")
            print(f"  Title: {job['title']}")
            print(f"  Company: {job['company']}")
            print(f"  Level: {job['level']}")
            print(f"  Location: {job['location']}")
            print(f"  Salary: {job['salary']}")
            print(f"  Age Requirement: {job['age_requirement']}")
            print(f"  Applied: {applied_status}")
            print(f"  Applicants Needed: {job['applicants_needed']}")
            print(f"  Current Applicants ({len(job['applicants'])}): {', '.join(job['applicants']) if job['applicants'] else 'None'}")
            if len(job["applicants"]) >= job["applicants_needed"]:
                print("  * This job has enough applicants. *")
            return
    print("Job not found.")

def show_all_jobs():
    if jobs:
        print("\nJob Opportunities:")
        for i, job in enumerate(jobs, start=1):
            applied_status = "Yes" if job["applied"] else "No"
            applicant_status = f"{len(job['applicants'])}/{job['applicants_needed']}"
            enough_msg = " *[Enough applicants]*" if len(job["applicants"]) >= job["applicants_needed"] else ""
            print(f"{i}. Job Title: {job['title']} | Company: {job['company']} | Level: {job['level']} | Location: {job['location']} | Salary: {job['salary']} | Age Req: {job['age_requirement']} | Applied: {applied_status} | Applicants: {applicant_status}{enough_msg}")
    else:
        print("No jobs available.")

def apply_to_job():
    title = input("Enter job title to apply for: ")
    name = input("Enter your name: ")
    for job in jobs:
        if job["title"].lower() == title.lower():
            if len(job["applicants"]) >= job["applicants_needed"]:
                print("Application closed. This job has enough applicants.")
                return
            if name in job["applicants"]:
                print("You have already applied to this job.")
            else:
                job["applicants"].append(name)
                job["applied"] = True
                print(f"{name} has applied to '{title}'.")
            return
    print("Job not found.")

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Job")
        print("2. Edit Job")
        print("3. Delete Job")
        print("4. Show All Jobs")
        print("5. Back to Main Menu")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            add_job()
        elif choice == '2':
            edit_job()
        elif choice == '3':
            delete_job()
        elif choice == '4':
            show_all_jobs()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

def applicant_menu():
    while True:
        print("\n--- Applicant Menu ---")
        print("1. View Jobs")
        print("2. Search Job")
        print("3. Apply for a Job")
        print("4. Back to Main Menu")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            show_all_jobs()
        elif choice == '2':
            search_job()
        elif choice == '3':
            apply_to_job()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

# MAIN SCREEN
while True:
    print("\n=== MAIN MENU ===")
    print("1. Admin")
    print("2. Applicant")
    print("3. Exit")

    main_choice = input("Enter choice (1-3): ")

    if main_choice == '1':
        if admin_username is None and admin_password is None:
            print("\n--- Admin Account Setup ---")
            admin_username = input("Create admin username: ")
            admin_password = input("Create admin password: ")
            print("Admin account created successfully! Please login now.\n")
        else:
            print("\n--- Admin Login ---")
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")

            if username == admin_username and password == admin_password:
                print("Admin login successful!")
                admin_menu()
            else:
                print("Invalid admin credentials. Returning to main menu.")

    elif main_choice == '2':
        applicant_menu()

    elif main_choice == '3':
        print("Goodbye! Good luck!")
        break

    else:
        print("Invalid choice. Try again.")