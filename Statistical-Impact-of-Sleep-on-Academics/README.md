# Statistically Exploring the Relationship Between Sleep and Academic Performance

## Project Overview
This project investigates the correlation between sleep quality and academic performance, specifically analyzing if attendance rates act as a mediating variable[cite: 3]. Originally developed for the INST627: Data Analytics for Information Professionals course at the University of Maryland[cite: 3], this analysis utilizes multiple regression models to answer two primary research questions:
* Do students who sleep more get better exam scores?[cite: 3]
* Can a student's attendance percentage mediate the relationship between sleep hours and academic performance?[cite: 3]

## The Dataset
* **Source:** A publicly available Kaggle dataset collected by Muhammad Shoaib (2025)[cite: 3].
* **Scale:** 200 data points representing individual students[cite: 3].
* **Variables Analyzed:** `student_id`, `sleep_hours`, `hours_studied`, `attendance_percent`, `previous_scores`, and `exam_scores`[cite: 3]. 

## Methodology
The analytical pipeline was structured to ensure statistical rigor before interpreting the relationships between variables:
* **Assumption Checking:** Verified linearity, normal distribution of residuals (via Normal Q-Q plots), and homoscedasticity (via Scale-Location plots) to ensure the validity of the linear regression models[cite: 3]. 
* **Pearson Correlation & Linear Regression:** Applied to observe the direct effect of sleep hours on exam scores[cite: 3].
* **Baron and Kenny (1986) Approach:** A classic regression-based method used to assess whether attendance percentage conceptually explains part of the relationship between sleep hours and exam performance[cite: 3].

## Key Findings
* **Direct Impact of Sleep:** There is a statistically significant, weakly positive association between a student's average hours of sleep and their exam scores[cite: 3]. The linear regression results indicate that each additional hour of sleep is associated with an approximate 0.85-point increase on the exam[cite: 3]. 
* **Mediation Failure:** Sleep hours did not significantly predict attendance percentage[cite: 3]. Because of this, the conditions for mediation were not met, meaning attendance does not mediate the relationship between sleep and exam scores[cite: 3]. 
* **Controlling for Prior Performance:** When controlling for previous academic scores, sleep hours remained a significant predictor of exam scores, highlighting that sleep has an independent positive relationship with exam performance[cite: 3]. 

## Limitations
* The dataset provided raw point values for exam scores without identifying the total possible points (e.g., graded out of 50 or 60), which limited the ability to determine exact student grades[cite: 3]. 
* Contextual variables, such as the specific university, course name, and course schedule, were not recorded in the dataset[cite: 3]. 

## Authors
* **Wonwoo Choi**[cite: 3]
* **Peter Zheng**[cite: 3]
* **Nisank Arunkumar**[cite: 3]
