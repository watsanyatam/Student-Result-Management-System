# Problem Statement

## Problem
Schools and colleges often record marks in scattered notebooks or spreadsheets.
Calculating totals, percentages, grades and class ranks by hand is slow and
error-prone, and there is no quick way to spot failing students, weak subjects
or how the class is performing overall. Wrong data (e.g. marks above 100, a
duplicated roll number) also slips in easily because nothing validates it.

## Proposed Solution
A **Student Result & Grade Management System**: a menu-driven, command-line
application written in pure Python that stores student records, validates every
input, automatically computes results and produces ready-to-read reports.

## Scope
**In scope**
- Create, view, update, delete and search student records.
- Enter, update and remove subject-wise marks (0-100).
- Automatic total, percentage, letter grade, GPA and PASS/FAIL result.
- Rank list (with tie handling), individual report cards, class and
  subject-wise analytics, grade distribution chart.
- Persistent JSON storage, CSV export, logging, input validation.

**Out of scope** (listed as future enhancements)
- Graphical or web interface, multi-user login, database server,
  PDF report cards, weighted/credit-based grading per subject.

## Target Users
- **Teachers / class coordinators** who enter marks and need quick reports.
- **Department office staff** who maintain records and export results.
- **Students of programming** who want a reference for a modular Python project.

## High-Level Features
1. **Student Management module** - add / view / update / delete / search students.
2. **Marks & Grade Processing module** - mark entry with validation; totals,
   percentages, grades, GPA, pass/fail, ranking.
3. **Reporting & Analytics module** - report cards, rank list, subject-wise
   statistics (average, high, low, std-dev, pass rate), grade distribution,
   class summary, CSV export.
4. **Cross-cutting** - JSON persistence with atomic saves, logging, custom
   exceptions, automated tests.


## Objectives

See `docs/02_objectives.md` for the complete project objectives.

## Formal Requirements

See `docs/01_requirements.md` for the functional and non-functional requirements.
