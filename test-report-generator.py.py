import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
import pickle
import os

# Function to save the last selected directories
def save_last_directories(last_file_path, last_save_directory):
    with open('last_directories.pkl', 'wb') as f:
        pickle.dump((last_file_path, last_save_directory), f)

# Function to load the last selected directories
def load_last_directories():
    if os.path.exists('last_directories.pkl'):
        with open('last_directories.pkl', 'rb') as f:
            return pickle.load(f)
    return None, None

def generate_report(file_path, save_directory):
    # Load the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the data from the 'data-raw' attribute
    data_raw = soup.body.get('data-raw')
    if data_raw is None:
        messagebox.showerror("Error", "No data-raw attribute found in the HTML file.")
        return

    data = json.loads(data_raw)

    # Extract test data
    stats = data['stats']
    total_tests = stats['tests']
    total_passes = stats['passes']
    total_failures = stats['failures']
    pass_percent = stats['passPercent']
    pass_percent = f"{pass_percent:.2f}"  
    pending = stats['pending']

    # Prepare data for the bar chart
    categories = ['Passed', 'Failed', 'Pending']
    values = [total_passes, total_failures, pending]

    # Create a DataFrame for better visualization
    df = pd.DataFrame({'Category': categories, 'Value': values})

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['Category'], df['Value'], color=['green', 'red', 'orange'])
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Test Results Summary')
    plt.grid(True)

    # Save the chart to the specified directory
    chart_file_path = f"{save_directory}/test_results_summary.png"
    plt.savefig(chart_file_path)
    plt.close()

    # Generate HTML report
    report_html = f"""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Test Report</title>
        <style>
            body {{ background-color: #333; color: #fff; font-family: Arial, sans-serif; }}
            .container {{ background-color: #fff; color: #000; padding: 20px; margin: 50px auto; max-width: 800px; border-radius: 10px; }}
            h1, h2 {{ text-align: center; }}
            .chart {{ text-align: center; }}
            .chart img {{ max-width: 100%; height: auto; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Test Report Summary</h1>
            <ul>
                <li>Total Tests: {total_tests}</li>
                <li>Passed: {total_passes}</li>
                <li>Failed: {total_failures}</li>
                <li>Pending: {pending}</li>
                <li>Pass Percentage: {pass_percent}%</li>
            </ul>
            <div class="chart">
                <img src="test_results_summary.png" alt="Test Results Summary">
            </div>
        </div>
    </body>
    </html>
    """

    # Save the HTML report
    report_file_path = f"{save_directory}/test_report.html"
    with open(report_file_path, 'w', encoding='utf-8') as report_file:
        report_file.write(report_html)

    messagebox.showinfo("Success", f"Report generated successfully at {report_file_path}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
    if file_path:
        entry_file_path.delete(0, 'end')
        entry_file_path.insert(0, file_path)
        save_last_directories(file_path, entry_save_directory.get())

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_save_directory.delete(0, 'end')
        entry_save_directory.insert(0, directory)
        save_last_directories(entry_file_path.get(), directory)

def on_generate_report():
    file_path = entry_file_path.get()
    save_directory = entry_save_directory.get()
    if not file_path or not save_directory:
        messagebox.showerror("Error", "Please select both the HTML file and the save directory.")
    else:
        generate_report(file_path, save_directory)
        save_last_directories(file_path, save_directory)

# Create the GUI application
app = Tk()
app.title("Test Report Generator")

label_file_path = Label(app, text="Select HTML file:")
label_file_path.pack(pady=5)

entry_file_path = Entry(app, width=50)
entry_file_path.pack(pady=5)

button_browse_file = Button(app, text="Browse", command=browse_file)
button_browse_file.pack(pady=5)

label_save_directory = Label(app, text="Select save directory:")
label_save_directory.pack(pady=5)

entry_save_directory = Entry(app, width=50)
entry_save_directory.pack(pady=5)

button_browse_directory = Button(app, text="Browse", command=browse_directory)
button_browse_directory.pack(pady=5)

button_generate_report = Button(app, text="Generate Report", command=on_generate_report)
button_generate_report.pack(pady=20)

# Load the last selected directories if they exist
last_file_path, last_save_directory = load_last_directories()
if last_file_path:
    entry_file_path.insert(0, last_file_path)
if last_save_directory:
    entry_save_directory.insert(0, last_save_directory)

app.mainloop()
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
import pickle
import os

# Function to save the last selected directories
def save_last_directories(last_file_path, last_save_directory):
    with open('last_directories.pkl', 'wb') as f:
        pickle.dump((last_file_path, last_save_directory), f)

# Function to load the last selected directories
def load_last_directories():
    if os.path.exists('last_directories.pkl'):
        with open('last_directories.pkl', 'rb') as f:
            return pickle.load(f)
    return None, None

def generate_report(file_path, save_directory):
    # Load the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the data from the 'data-raw' attribute
    data_raw = soup.body.get('data-raw')
    if data_raw is None:
        messagebox.showerror("Error", "No data-raw attribute found in the HTML file.")
        return

    data = json.loads(data_raw)

    # Extract test data
    stats = data['stats']
    total_tests = stats['tests']
    total_passes = stats['passes']
    total_failures = stats['failures']
    pass_percent = stats['passPercent']
    pass_percent = f"{pass_percent:.2f}"  # Format pass percentage with 2 decimal places
    pending = stats['pending']

    # Prepare data for the bar chart
    categories = ['Passed', 'Failed', 'Pending']
    values = [total_passes, total_failures, pending]

    # Create a DataFrame for better visualization
    df = pd.DataFrame({'Category': categories, 'Value': values})

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['Category'], df['Value'], color=['green', 'red', 'orange'])
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Test Results Summary')
    plt.grid(True)

    # Save the chart to the specified directory
    chart_file_path = f"{save_directory}/test_results_summary.png"
    plt.savefig(chart_file_path)
    plt.close()

    # Generate HTML report
    report_html = f"""
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Test Report</title>
        <style>
            body {{ background-color: #333; color: #fff; font-family: Arial, sans-serif; }}
            .container {{ background-color: #fff; color: #000; padding: 20px; margin: 50px auto; max-width: 800px; border-radius: 10px; }}
            h1, h2 {{ text-align: center; }}
            .chart {{ text-align: center; }}
            .chart img {{ max-width: 100%; height: auto; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Test Report Summary</h1>
            <ul>
                <li>Total Tests: {total_tests}</li>
                <li>Passed: {total_passes}</li>
                <li>Failed: {total_failures}</li>
                <li>Pending: {pending}</li>
                <li>Pass Percentage: {pass_percent}%</li>
            </ul>
            <div class="chart">
                <img src="test_results_summary.png" alt="Test Results Summary">
            </div>
        </div>
    </body>
    </html>
    """

    # Save the HTML report
    report_file_path = f"{save_directory}/test_report.html"
    with open(report_file_path, 'w', encoding='utf-8') as report_file:
        report_file.write(report_html)

    messagebox.showinfo("Success", f"Report generated successfully at {report_file_path}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
    if file_path:
        entry_file_path.delete(0, 'end')
        entry_file_path.insert(0, file_path)
        save_last_directories(file_path, entry_save_directory.get())

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        entry_save_directory.delete(0, 'end')
        entry_save_directory.insert(0, directory)
        save_last_directories(entry_file_path.get(), directory)

def on_generate_report():
    file_path = entry_file_path.get()
    save_directory = entry_save_directory.get()
    if not file_path or not save_directory:
        messagebox.showerror("Error", "Please select both the HTML file and the save directory.")
    else:
        generate_report(file_path, save_directory)
        save_last_directories(file_path, save_directory)

# Create the GUI application
app = Tk()
app.title("Test Report Generator")

label_file_path = Label(app, text="Select HTML file:")
label_file_path.pack(pady=5)

entry_file_path = Entry(app, width=50)
entry_file_path.pack(pady=5)

button_browse_file = Button(app, text="Browse", command=browse_file)
button_browse_file.pack(pady=5)

label_save_directory = Label(app, text="Select save directory:")
label_save_directory.pack(pady=5)

entry_save_directory = Entry(app, width=50)
entry_save_directory.pack(pady=5)

button_browse_directory = Button(app, text="Browse", command=browse_directory)
button_browse_directory.pack(pady=5)

button_generate_report = Button(app, text="Generate Report", command=on_generate_report)
button_generate_report.pack(pady=20)

# Load the last selected directories if they exist
last_file_path, last_save_directory = load_last_directories()
if last_file_path:
    entry_file_path.insert(0, last_file_path)
if last_save_directory:
    entry_save_directory.insert(0, last_save_directory)

app.mainloop()
