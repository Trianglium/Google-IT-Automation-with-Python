<h1 align="center">Log Analysis Using Regular Expressions</h1>
<p align="center"><strong>Automation scripts meant to process system log events, generate CSV files based on the information extracted, and visualize the findings.</strong>

<h2>Problem Statement</h2>

<em>Imagine your company uses a server that runs a service called ticky, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need your help getting some information from those logs so that they can better understand how their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will process the system log and generate reports based on the information extracted from the log files.</em>

<h2>Project Objectives</h2>

- Use regex to parse a log file
- Append and modify values in a dictionary
- Write to a file in CSV format
- Move files to the appropriate directory for use with the CSV->HTML converterm log events, generate CSV files based on the information extracted, and visualize the findings.

<h2>Example Usage</h2>

## [error_message.csv](System-Log-Analysis/error_message.csv)
###  ![error message visualization](https://user-images.githubusercontent.com/70343977/136632176-6ce00c83-5123-4eba-9ecf-bd889984391e.png)

## __[user_statistics.csv](System-Log-Analysis/user_statistics.csv)__
### ![user_statistics_visualization](https://user-images.githubusercontent.com/70343977/136632206-7e955802-dde0-49ac-a157-3e82069dd0c2.png)
