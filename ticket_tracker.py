records = []

def display_menu():
    """ Runs the main to display the menu loop until Exit.

    Parameters: none.
    Returns: None.
    """
    # Why the loop only ends on option 7
    print('''
--- Event Ticket Sales Tracker ---
1. Record Sale
2. Record Refund
3. List Records
4. Delete Record
5. View Overall Summary
6. View Summary by Ticket Type
7. Exit
''')


def add_record(current_records, record_type):
    """Prompt for record details and to append a new record.

    Parameters: current_records (list): the list of record dictionaries to append to.
                record_type (str): either "Sale" or "Refund".
    Returns: None.
    """
    amount_text = input(f"Enter {record_type.lower()} amount: ").strip()

    try:
        amount = float(amount_text)
    except ValueError:
        print("Invalid amount. Please enter a positive number.")
        return
    # Why the second check also catches nan
    if not amount > 0:
        print("Invalid amount. Please enter a positive number.")
        return

    event = input("Enter event name: ").strip()
    if event == "":
        print("Invalid event name. The event name cannot be empty.")
        return

    ticket_type = input("Enter ticket type: ").strip()

    record = {
        "type": record_type,
        "amount": amount,
        "event": event,
        "ticket_type": ticket_type,
    }
    current_records.append(record)
    print(f"{record_type} of £{amount:.2f} for {event} "
          f"(Ticket type: {ticket_type}) recorded.")


def list_records(records):
    """Print all records.

    Parameters:
        records (list): of records.
    Returns:
        None.
    """
    if len(records) == 0:
        print("No records found.")
        return

    print("--- All Records ---")
    number = 1
    for record in records:
        print(f"{number}. [{record['type']}] - £{record['amount']:.2f} - "
              f"{record['event']} (Ticket type: {record['ticket_type']})")
        number += 1


def delete_record(records):
    """Delete a record.

    Parameters:
        records (list): the list of records.
    Returns:
        None.
    """
    if len(records) == 0:
        print("There are no records to delete.")
        return

    list_records(records)
    choice_text = input("Enter the number of the record to delete "
                        "(0 to cancel): ").strip()

    try:
        choice = int(choice_text)
    except ValueError:
        print(f"Invalid number. Please enter a number from 1 to {len(records)}.")
        return

    if choice == 0:
        print("Deletion cancelled. No records were deleted.")
        return

    # Reject out-of-range numbers
    if choice < 1 or choice > len(records):
        print(f"Invalid number. Please enter a number from 1 to {len(records)}.")
        return

    removed = records.pop(choice - 1)
    print(f"Deleted record {choice}: [{removed['type']}] - "
          f"£{removed['amount']:.2f} - {removed['event']} "
          f"(Ticket type: {removed['ticket_type']})")


def calculate_summary(records):
    """Calculate overall sales figures from the records.

    Parameters:
        records (list): list of records.

    Returns:
        dict: {"total_sales": float, "total_refunds": float,
               "net_revenue": float, "sales_count": int}
    """
    total_sales = 0.0
    total_refunds = 0.0
    sales_count = 0

    # Why refunds are added to their own total rather than subtracted from sales
    for record in records:
        if record["type"] == "Sale":
            total_sales += record["amount"]
            sales_count += 1
        elif record["type"] == "Refund":
            total_refunds += record["amount"]

    return {
        "total_sales": total_sales,
        "total_refunds": total_refunds,
        "net_revenue": total_sales - total_refunds,
        "sales_count": sales_count,
    }


def print_overall_summary(summary_data):
    """Print overall summary.

    Parameters:
        summary_data (dict): dictionary returned by calculate_summary().

    Returns:
        None
    """
    print("\n--- Overall Summary ---")
    print(f"Total sales: £{summary_data['total_sales']:.2f}")
    print(f"Total refunds: £{summary_data['total_refunds']:.2f}")
    print(f"Net revenue: £{summary_data['net_revenue']:.2f}")
    print(f"Number of sales: {summary_data['sales_count']}")


def print_summary_by_ticket_type(records):
    """Print net revenue for each unique ticket type.

    Parameters:
        records (list): list of record dictionaries.

    Returns:
        None
    """
    net_by_type = {}

    for record in records:
        ticket_type = record["ticket_type"]
        if ticket_type not in net_by_type:
            net_by_type[ticket_type] = 0.0  # Why a ticket type starts at 0.0 the first time it is seen

        if record["type"] == "Sale":
            net_by_type[ticket_type] += record["amount"]
        elif record["type"] == "Refund":
            net_by_type[ticket_type] -= record["amount"]

    print("\n--- Net Revenue by Ticket Type ---")
    if not net_by_type:
        print("No records found.")
    else:
        for ticket_type in net_by_type:
            print(f"{ticket_type}: £{net_by_type[ticket_type]:.2f}")
    print("----------------------------------")


def main():
    """Print the main menu

    Parameters: none
    returns: none
    """
    while True:
        display_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            add_record(records, "Sale")
        elif choice == "2":
            add_record(records, "Refund")
        elif choice == "3":
            list_records(records)
        elif choice == "4":
            delete_record(records)
        elif choice == "5":
            print_overall_summary(calculate_summary(records))
        elif choice == "6":
            print_summary_by_ticket_type(records)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()