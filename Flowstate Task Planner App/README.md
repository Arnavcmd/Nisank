# FlowState: An AI Adaptive Student Planner

## Project Overview

FlowState is an AI-adaptive student planner designed to address the problem of students missing deadlines due to feeling overwhelmed[cite: 4]. Traditional apps often show a "wall of text" with many tasks, which can increase anxiety and lead to a state of "freezing" or "decision fatigue" where students spend more time planning than studying[cite: 4]. FlowState solves this by combining the speed of automation with strict human verification, ensuring tasks are managed effectively without sacrificing trust[cite: 4].

**Role:** Product Designer[cite: 4]
**Tools Used:** ChatGPT & Gemini (AI Co-Pilots), Figma (Design), React & Tailwind CSS (Development)[cite: 4]
**Timeline:** Fall 2025[cite: 4]

## The Core Strategy: "Zero-Red"

By utilizing ChatGPT as a "Lead Researcher," the project identified that traditional UI patterns, such as red notification badges, can spike anxiety[cite: 4]. This insight guided the core "Zero-Red" strategy to minimize cognitive load[cite: 4].

## The 3-Step Flow Solution

FlowState uses a simple 3-step process to reduce anxiety and improve focus:

1.  **Parse:** Users drag and drop a syllabus (supports TXT files, no API keys needed), and the AI instantly extracts assignments, deadlines, effort estimates, and energy levels[cite: 4].
2.  **Filter:** The app prompts the user with "How is your energy right now?" offering "Low" (Brain Dead), "Medium" (Okay), or "High" (Ready to Grind) options[cite: 4].
3.  **Focus:** Based on the selected energy level, the app hides the noise and presents only 2-3 relevant tasks in the "Smart Queue" (Dashboard)[cite: 4].

## "Human-in-the-Loop" Verification

AI is great at data but can lack empathy, leading to errors like rating a "Midterm Research Paper" as "Low Energy" (20 mins) just because its description is short[cite: 4]. To prevent these "AI Hallucinations," FlowState features a "Human-in-the-Loop Verification Screen"[cite: 4]. 

*   Users are required to review AI-generated estimates and can override them[cite: 4].
*   Confidence badges indicate if the AI's confidence is less than 90%, forcing the user to verify the data[cite: 4].
*   Users can also manually input tasks[cite: 4].

## Features

*   **Smart Syllabus Parsing:** Automatically detects assignments and exams, parses due dates and descriptions, and estimates effort and energy levels[cite: 4].
*   **Energy Engine:** Filters tasks based on current energy levels (Low, Medium, High)[cite: 4].
*   **The Smart Queue (Dashboard):** An anti-anxiety interface that shows only 2-3 relevant tasks. Hovering over a task reveals a "Focus" button, keeping the UI clean[cite: 4].
*   **Profile and Stats Screens:**
    *   Tracks day streaks, tasks completed today, total tasks done, and time saved[cite: 4].
    *   Displays overall progress[cite: 4].
    *   Provides real data charts that update live based on actual completion timestamps[cite: 4].
    *   Offers insights into energy distribution (e.g., Low vs. High energy tasks completed), top courses, and the most productive days, all derived from real usage patterns[cite: 4].

## Author

**Nisank Arunkumar**[cite: 4]
Email: narnav1@umd.edu[cite: 4]
