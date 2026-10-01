
import streamlit as st
# Grade calculation

def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

st.title("Student Grade Manager")

if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add_student"):
    name = st.text_input("Name")
    mark = st.number_input("Mark",min_value=0,max_value=100)
    add_student = st.form_submit_button("Add")

# Add student when button is clicked
if add_student:
    if not name.strip():
        st.error("Please enter a student name.")
    else:
        grade = get_grade(mark)

        student = {
        "Name": name,
        "Mark": mark,
        "Grade": grade
        }

        st.session_state.students.append(student)
        st.success("Student added successfully!")

# Display students and statistics

if st.session_state.students:
    st.subheader("Students")
    st.table(st.session_state.students)

    # Get all marks
    marks = [student["Mark"]for student in st.session_state.students]

    # Calculate class statistics
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Display metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Average", round(average, 1))
    col2.metric("Highest", highest)
    col3.metric("Lowest", lowest)