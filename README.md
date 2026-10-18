# CS5097_Ticket_Tracker

## Overview
This ticket tracker programme is a console application that lets an event venue record sales, record refunds, list and delete records, and view two summaries. Data is stored only in memory. 

## How to run the programme
To run the console application, you need Python 3.12.3 installed on your computer. Then, run `python3 ticket_tracker.py` in the terminal.

## Assumptions and limitations
- When the programme closes, data gets lost 
- An empty ticket type is allowed
- When an invalid delete number is entered, the app returns to the menu
- Standard and standard count as different ticket types
- The programme accepts `inf` as an amount, which would produce meaningless totals

## Test plan
- Input: I entered -20 as sale amount - Result: Invalid amount. Please enter a positive number.
- Input: I did not enter any event name - Result: Invalid event name. The event name cannot be empty.
- Input: I choose option 3 on the menu - Result: No records found.
- Input: With one record stored, I entered 9 at the delete prompt - Result: Invalid number. Please enter a number from 1 to 1
- Input: I entered all task 4 records and opt for option 5 on the menu - Result: 
```
--- Overall Summary ---
Total sales: £185.00
Total refunds: £45.00
Net revenue: £140.00
Number of sales: 3
```

## Completion report
- Task 2 completed: the menu repeats until the user selects Exit. If a user enters a choice that is not on the menu, it would print Invalid choice. Please enter a number from 1 to 7.
- Task 3 completed. If a user enters empty event name, the app would output: Invalid event name. The event name cannot be empty. Also, it rejects non-numeric, zero and negative amounts.
- Task 4 completed. It successfully displays all recorded sales and refunds in a clear numbered list.
- Task 5 completed: enables the user to remove a specific record by index with option to cancel and it also handles out of range input as well as non-numeric input, entering 0 cancels with a message which returns to the menu after an error.
- Task 6 completed: successfully provides overall summary and a breakdown of net revenue by ticket type using loops and dictionary with no `sum()` or `Counter`