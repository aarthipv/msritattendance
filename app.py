import streamlit as st

def calculate_attendance_data(present, absent, remaining):
    total = present + absent + remaining

    percent = (present / (total - remaining)) * 100 if total - remaining > 0 else 0

    bunk_75 = int(0.25 * total) - absent  
    bunk_80 = int(0.20 * total) - absent

    if bunk_75 < 0:
            bunk_75 = "Attendance too low"
        
    if bunk_80 < 0:
            bunk_80 = "Attendance low"

    return {
        'total': total,
        'percent': int(percent),
        'bunk_75': bunk_75,
        'bunk_80': bunk_80
    }

def main():
    st.title("Attendance Calculator")

    present = st.number_input("Number of Classes Present", step=1)
    absent = st.number_input("Number of Classes Absent", step=1)
    remaining = st.number_input("Number of Classes Remaining", step=1)

    if st.button("Calculate"):
        calculated_data = calculate_attendance_data(present, absent, remaining)

        st.write(f"Total Classes: {calculated_data['total']}")
        st.write(f"Attendance Percentage: {calculated_data['percent']}%")
        st.write(f"Max Bunk for 75%: {calculated_data['bunk_75']}")
        st.write(f"Max Bunk for 80%: {calculated_data['bunk_80']}")

if __name__ == "__main__":
    main()