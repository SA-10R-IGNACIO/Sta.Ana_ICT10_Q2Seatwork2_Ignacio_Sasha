from pyscript import display, document

def general_weighted_average(e):
    # Clear previous content
    document.getElementById('student_info').innerHTML = ''
    document.getElementById('summary').innerHTML = ''
    document.getElementById('output').innerHTML = ''

    # Get student info
    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()

    # Retrieve and convert grades
    try:
        filipino = float(document.getElementById('filipino').value)
        english = float(document.getElementById('english').value)
        math = float(document.getElementById('math').value)
        science = float(document.getElementById('science').value)
        social = float(document.getElementById('social').value)
        values = float(document.getElementById('values').value)
        ict = float(document.getElementById('ict').value)
        pe = float(document.getElementById('pe').value)
    except ValueError:
        display("⚠️ Please enter valid numbers for all grades.", target="output")
        return

    # Create dictionary for subjects
    subjects = {
        "Filipino": filipino,
        "English": english,
        "Mathematics": math,
        "Science": science,
        "Social Studies": social,
        "Values Education": values,
        "ICT": ict,
        "PE": pe
    }

    # Compute GWA
    gwa = sum(subjects.values()) / len(subjects)

    # Create summary display
    summary_text = "\n".join([f"{subject}: {grade:.0f}" for subject, grade in subjects.items()])

    # Display results
    display(f"🌸 Student: {first_name} {last_name}", target="student_info")
    display(summary_text, target="summary")
    display(f"🌿 Your General Weighted Average is: {gwa:.2f}", target="output")
