def generate_report(title, *args, **kwargs):
    print("Report Title:",title)
    print("=====================================\n")
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    print("Report Sections:")
    print("--------------------------------\n")
    for i in range(0,len(args)):
        if i == 0:
            print("Section 1:",args[0])
        elif i == 1:
            print("Section 2:", args[1])
        else:
            print(f"Conclusion: \n-----------------------------------------\n {args[2]}")

    with open("file.txt","w") as file:
        file.write(f"Report Title: Monthly Sales Report \n =====================================\n Author: John Doe \n Date: August 2024\n Report Sections:\n --------------------------------\n Section 1: Introduction: Overview of sales performance.\n Section 2: Market Trends: Analysis of current market trends.\n Conclusion: \n ----------------------------------------\n Overall, sales have increased by 15% compared to previous month.")

generate_report("Monthly Sales Report","Introduction: Overview of sales performance.","Market Trends: Analysis of current market trends.","Overall, sales have increased by 15% compared to previous month",Author="John Doe", Date="August 2024")


















































































































