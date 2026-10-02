"""Run: python -m streamlit run student_grade_app.py"""
import csv
import io
from html import escape
import streamlit as st

st.set_page_config(page_title="Grade Studio", page_icon="🎓", layout="centered")
st.markdown('''<style>
.stApp {background:radial-gradient(ellipse at top left,#ede9fe,transparent 55%),#f8fafc;color:#172033;}
.block-container {max-width:960px;padding-top:3rem;}
h1,h2,h3 {color:#172033!important;}
.eyebrow {color:#7c3aed;font-size:12px;letter-spacing:3px;font-weight:700;}
.hero {font-size:48px;letter-spacing:-2px;font-weight:800;}
.subtitle {color:#64748b;margin:8px 0 28px;}
[data-testid="stForm"] {background:white;border:1px solid #e2e8f0;border-radius:24px;padding:28px;box-shadow:0 18px 50px #1720330a;}
.stFormSubmitButton button {background:#7c3aed;color:white;border:0;border-radius:12px;min-height:48px;}
[data-testid="stMetric"] {background:white;padding:20px;border:1px solid #e2e8f0;border-radius:18px;}
.banner {background:linear-gradient(120deg,#5b21b6,#7c3aed,#2563eb);color:white;padding:28px;border-radius:24px;margin:24px 0;}
.banner h2 {color:white!important;margin:0;}
.banner p {margin:8px 0 0;opacity:.9;}
</style>''', unsafe_allow_html=True)

SUBJECTS = ["English", "Mathematics", "Science", "Social Science", "Computer Science"]

def grade_for(percentage):
    for minimum, grade in [(90,"A+"),(80,"A"),(70,"B"),(60,"C"),(50,"D"),(40,"E")]:
        if percentage >= minimum:
            return grade
    return "F"

st.markdown('<div class="eyebrow">LEARN • GROW • ACHIEVE</div><div class="hero">Grade Studio 🎓</div><div class="subtitle">Turn student marks into a clear picture of progress.</div>', unsafe_allow_html=True)
st.caption("Each subject is out of 100. A student passes only when every subject is at least 40. These are sample grading rules; use your school’s policy if different.")

with st.form("student_form"):
    st.subheader("Student details")
    left, right = st.columns(2)
    with left:
        name = st.text_input("Student name", placeholder="Enter student name")
    with right:
        roll = st.text_input("Roll number", placeholder="e.g. STU001")
    st.subheader("Subject marks")
    marks = {}
    columns = st.columns(2)
    for index, subject in enumerate(SUBJECTS):
        with columns[index % 2]:
            marks[subject] = st.number_input(subject, min_value=0, max_value=100, value=0, step=1, key=subject)
    submitted = st.form_submit_button("Generate grade report →", use_container_width=True)

if submitted:
    if not name.strip() or not roll.strip():
        st.session_state.pop("report", None)
        st.error("Please enter both the student name and roll number.")
    else:
        st.session_state.report = {"name": name.strip(), "roll": roll.strip(), "marks": marks.copy()}

if "report" in st.session_state:
    report = st.session_state.report
    scores = report["marks"]
    total = sum(scores.values())
    percentage = total / len(scores)
    passed = all(mark >= 40 for mark in scores.values())
    grade = grade_for(percentage) if passed else "F"
    status = "PASS" if passed else "NEEDS IMPROVEMENT"
    st.markdown(f'<div class="banner"><h2>{escape(report["name"])} · Grade {grade}</h2><p>Roll number: {escape(report["roll"])} · {status}</p></div>', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    a.metric("Total marks", f"{total} / {len(scores)*100}")
    b.metric("Percentage", f"{percentage:.2f}%")
    c.metric("Subjects passed", f"{sum(v >= 40 for v in scores.values())} / {len(scores)}")
    st.progress(percentage / 100, text="Overall score")
    if passed:
        st.success("All subjects passed. Keep building on your progress!")
    else:
        failed = ", ".join(subject for subject, mark in scores.items() if mark < 40)
        st.warning(f"Focus on: {failed}. At least 40 marks are required in every subject to pass.")
    rows = [{"Subject": subject, "Marks / 100": mark, "Grade": grade_for(mark), "Status": "Pass" if mark >= 40 else "Fail"} for subject, mark in scores.items()]
    st.subheader("Subject performance")
    st.dataframe(rows, hide_index=True, use_container_width=True)
    st.bar_chart(scores, color="#7c3aed")
    best = max(scores.values())
    st.caption("Highest scoring subject(s): " + ", ".join(s for s,v in scores.items() if v == best))
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    # Prefix spreadsheet formula-like user input to keep the CSV safe to open.
    def csv_text(value):
        return "'" + value if value.lstrip().startswith(("=", "+", "-", "@")) else value
    writer.writerow(["Student name", csv_text(report["name"])])
    writer.writerow(["Roll number", csv_text(report["roll"])])
    writer.writerow([])
    writer.writerow(["Subject", "Marks / 100", "Grade", "Status"])
    writer.writerows([[r["Subject"],r["Marks / 100"],r["Grade"],r["Status"]] for r in rows])
    writer.writerow([])
    writer.writerows([["Total", total], ["Percentage", f"{percentage:.2f}%"], ["Overall grade", grade], ["Result", "Pass" if passed else "Fail"]])
    st.download_button("Download student report ↓", buffer.getvalue().encode("utf-8-sig"), "student_grade_report.csv", "text/csv", use_container_width=True)
    st.caption("Results reflect the last submitted marks. Click Generate grade report after editing.")
else:
    st.info("Fill in the student details and marks, then generate your report.")

with st.expander("Grading scale"):
    st.table([{ "Percentage": band, "Grade": grade} for band,grade in [("90–100","A+"),("80–below 90","A"),("70–below 80","B"),("60–below 70","C"),("50–below 60","D"),("40–below 50","E"),("Below 40","F")]])
    st.caption("Overall grade is F if any subject is below 40, regardless of the average.")
st.caption("Grade Studio · Reports stay in the current session unless downloaded.")
