# Student Result & Grade Management System

A modular, menu-driven **command-line application in pure Python** for managing
student records, entering marks, calculating grades and generating reports.
Built as the project for **VITyarthi - Python Essentials 2**.

## Overview
Teachers enter students and their subject marks; the system validates every
input, calculates totals / percentages / grades / GPA / pass-fail results,
ranks the class and produces analytics. Data is saved automatically to a JSON
file and can be exported to CSV.

## Features
- **Student management (CRUD):** add, view, update, delete and search students
- **Marks entry:** any number of subjects per student, validated to 0-100
- **Automatic processing:** total, percentage, letter grade (O/A+/A/B/C/D/F),
  GPA, PASS/FAIL (a student must clear every subject)
- **Reports:** individual report card, class rank list (ties share a rank),
  class summary, subject-wise statistics, grade-distribution chart
- **Persistence:** atomic JSON saves after every change; CSV export
- **Robustness:** strict input validation, custom exceptions, corrupt-file
  protection, logging to `logs/app.log`
- **47 automated tests** (unit tests + scripted end-to-end tests of the menu)

## Technologies Used
- Python 3.9+ (standard library only: `json`, `csv`, `re`, `array`, `logging`,
  `argparse`, `unittest`, `os`, `math`)
- Git / GitHub for version control

## Python Concepts Demonstrated
| Course module | Where it is used |
|---|---|
| Fundamentals, Operators, Precedence | Grade / percentage / std-dev formulas in `calculator.py` |
| Input & Output, Type Conversion | Menu prompts, `float()` conversion of marks, formatted reports |
| Core Data Structures | `dict` (students by roll no, marks by subject), `list`, `set`, `tuple` (`GRADE_SCALE`) |
| Control Flow | Menu loop, validation re-prompt loops, ranking logic |
| Functions | Validators, calculator functions, report builders |
| Modules & Packages | `app/` package with 10 modules |
| Arrays | `array('d')` for numeric series in statistics |
| OOP | `Person` -> `Student` inheritance, properties and defensive-copy access, overridden `describe()` (polymorphism), class method `from_dict()` |

For a module-by-module mapping to the supplied 13-module syllabus, see [`docs/syllabus_alignment.md`](docs/syllabus_alignment.md). Module 13 is left unassessed because its lesson titles were not provided.

## Project Structure
```
student_result_system/
├── main.py               # entry point
├── README.md
├── statement.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── cli.py            # menu loop and prompts
│   ├── manager.py        # CRUD operations (StudentManager)
│   ├── models.py         # Person, Student classes
│   ├── calculator.py     # totals, grades, ranking, statistics
│   ├── reports.py        # formatted text reports
│   ├── validators.py     # input validation
│   ├── storage.py        # JSON load/save, CSV export
│   ├── logger.py         # logging setup
│   └── exceptions.py     # custom exceptions
├── tests/                # unittest suite
├── data/sample_students.json
└── docs/                 # diagrams, sample output
```

## Installation & Running
```bash
git clone <your-repo-url>
cd student_result_system

# optional: start with the sample data
cp data/sample_students.json data/students.json

python main.py                       # uses data/students.json
python main.py --data other.json     # use a different data file
```
No packages need to be installed.

## Testing
```bash
python -m unittest discover -v
```
The tests use temporary folders, so they never touch your real data or logs.

## Sample Output
Real output from the application (see `docs/sample_session.txt` for a full session):

```
====================================================================
                        STUDENT REPORT CARD
====================================================================
Roll No : CS103
Name    : Chitra Nair
Course  : B.Tech CSE
--------------------------------------------------------------------
Subject                            Marks   Grade  Points
--------------------------------------------------------------------
English                            94.00       O      10
Mathematics                        91.00       O      10
Physics                            89.00      A+       9
Python                             95.00       O      10
--------------------------------------------------------------------
Total       : 369 / 400
Percentage  : 92.25%
Grade       : O
GPA         : 9.75
Result      : PASS
```

```
Rank  Roll No   Name                     Total        %  Gr Result
--------------------------------------------------------------------
1     CS103     Chitra Nair                369    92.25  O  PASS
2     CS101     Asha Rao                   343    85.75  A+ PASS
3     CS105     Esha Kapoor                320    80.00  A+ PASS
...
```
Add your own terminal screenshots to `docs/` and link them here.

## Grading Scale
| Percentage | Grade | Points |
|---|---|---|
| 90-100 | O | 10 |
| 80-89.99 | A+ | 9 |
| 70-79.99 | A | 8 |
| 60-69.99 | B | 7 |
| 50-59.99 | C | 6 |
| 40-49.99 | D | 5 |
| below 40 | F | 0 |

Pass mark: 40 in **every** subject.


## VITyarthi Submission Documents

The `docs/` directory contains the formal requirements, objectives, architecture, workflow, UML/design diagrams, storage design, testing evidence, challenges, learnings, future enhancements and references required by the project brief.

### Design diagrams
- `docs/diagrams/architecture.png`
- `docs/diagrams/workflow.png`
- `docs/diagrams/use_case.png`
- `docs/diagrams/class_diagram.png`
- `docs/diagrams/sequence_diagram.png`
- `docs/diagrams/storage_design.png`

### Screenshots
- `docs/screenshots/01_menu.png`
- `docs/screenshots/02_students.png`
- `docs/screenshots/03_report_card.png`
- `docs/screenshots/04_rank_list.png`
- `docs/screenshots/05_analytics.png`

See `PROJECT_REPORT.pdf` for the complete submission report.
