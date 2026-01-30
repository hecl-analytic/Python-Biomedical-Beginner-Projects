# Biomedical Python Portfolio

Welcome to my portfolio of beginner Python projects focused on **Biomedical Engineering** and **Health Data Analysis**. This repository demonstrates my journey from basic Python scripting to Object-Oriented Programming (OOP), applied to medical datasets.

## Projects Overview

### 1. Hematology Reporter (OOP)
**Location:** [./01_Hematology_Reporter_OOP](./01_Hematology_Reporter_OOP)
**Focus:** Object-Oriented Programming, Logic Encapsulation

A simulation of a Laboratory Information System (LIS) that models a patient's blood count using Python Classes.
- **Functionality:** Reads raw patient data (Hemoglobin, Leukocytes) from a file, creates `Patient` objects, and automatically evaluates health status based on medical norms.
- **Key Features:**
  - `Patient` class encapsulates medical data and diagnostic logic.
  - Dynamic sorting into risk categories (e.g., "High Risk", "Normal").
  - Generates a structured text protocol for doctors.

### 2. Health Calculators & Statistics
**Location:** [./02_Health_Calculators](./02_Health_Calculators)
**Focus:** Algorithms, Data Processing, Statistics

A set of tools for analyzing population health metrics from unstructured datasets.
- **BMI Analyzer:** Calculates Body Mass Index, classifies obesity levels according to WHO standards, and computes dataset statistics (Median, Mean, Min/Max).
- **Cholesterol Analyzer:** Evaluates cardiovascular risk based on cholesterol levels, automatically filtering out irrelevant data (e.g., Glucose tests) during processing.
- **Key Concepts:** Robust error handling (try-except), data cleaning, and file I/O operations.

### 3. Log Parser
**Location:** [./03_Log_Parser](./03_Log_Parser)
**Focus:** String Manipulation, ETL (Extract, Transform, Load)

A utility script designed to parse raw, unstructured server logs from medical devices.
- **Functionality:** Converts messy text logs into structured dictionaries/lists for further analysis.
- **Key Features:** Extracts Patient IDs, Heart Rate (HR), and Device Status from raw string formats. Demonstrates essential skills for cleaning "dirty" medical data.

---

## Technology Stack
* **Language:** Python 3.x
* **Core Concepts:** OOP, Algorithms, Data Structures (Lists, Dictionaries), File Handling.
* **Future Goals:** Transitioning these logics into Pandas & NumPy for large-scale analysis.

---
Created by Vojtech | Biomedical Engineering Student
