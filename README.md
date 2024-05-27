# Test Report Generator

This is a Python application that generates an HTML report from a given HTML file containing test data. The report includes a summary of the test results and a bar chart visualization.

## Prerequisites

- Python 3.x (Download and install from [python.org](https://www.python.org/downloads/))
- The following Python libraries:
  - `beautifulsoup4`
  - `matplotlib`
  - `pandas`
  - `tkinter`

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/test-report-generator.git
    cd test-report-generator
    ```
3. Install the required Python libraries:
    ```bash
    pip install beautifulsoup4 matplotlib pandas
    ```

## Usage

1. Run the application:
    ```bash
    python test_report_generator.py
    ```

2. Use the GUI to select the HTML file containing the test data and the directory where you want to save the generated report.

3. Click on the "Generate Report" button. The application will create an HTML report in the specified directory.

## How It Works

- The application uses `tkinter` to create a GUI for selecting the input HTML file and the output directory.
- It reads the input HTML file and extracts test data from the `data-raw` attribute.
- It generates a bar chart showing the summary of the test results using `matplotlib`.
- The application then creates an HTML report containing the test summary and the bar chart image.
- The last selected file path and save directory are saved in a configuration file (`config.json`) and loaded the next time the application runs.

## Project Structure

- `test_report_generator.py`: The main application script.
- `config.json`: Configuration file to save the last selected file path and save directory.

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss any changes you would like to make.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
