# Rapid Visual Screening Model

A Python-based application for analyzing and predicting the probability of failure in RC (Reinforced Concrete) buildings using machine learning algorithms.

## Features

- Interactive GUI interface for data input and analysis
- Building probability assessment
- Parameter-based failure prediction
- Database management for building data
- Visual progress indicators
- Comprehensive reporting system

## Prerequisites

Before running the application, make sure you have the following installed on your Windows system:

1. Python 3.8 or higher
2. pip (Python package installer)

## Installation

1. Clone or download this repository to your local machine.

2. Open Command Prompt as administrator and navigate to the project directory:
```cmd
cd path\to\project\folder
```

3. Create a virtual environment (recommended):
```cmd
python -m venv venv
venv\Scripts\activate
```

4. Install the required packages:
```cmd
pip install PySimpleGUI pandas openpyxl
```

## Required Files

Make sure you have the following files in your project directory:
- Welcome.py (Main entry point)
- WINDOW 2.PY
- WINDOW 3.PY
- code8.py
- DATABASEAREA.xlsx (Database file)
- dbsolve.xlsx (Parameters file)

## Running the Application

There are two ways to run the application:

### Option 1: Run the Building Probability Calculator directly

1. Make sure you're in the project directory with the virtual environment activated.

2. Run the building probability calculator:
```cmd
python code8.py
```

This will open the Building Probability Excel Creator where you can:
- Add buildings and their probability percentages
- Create and view the building database
- Calculate mean probability of failure
- Export data to Excel

### Option 2: Run the complete Rapid Visual Screening Model

1. Make sure you're in the project directory with the virtual environment activated.

2. Run the main application:
```cmd
python Welcome.py
```

3. The application will open with a welcome screen showing:
   - Project title
   - Team members
   - Project objectives

4. Click "Start" to proceed to the building selection page.

5. Select "RC" to begin the analysis process.

## Application Flow

1. **Welcome Screen**
   - View project information
   - Start the analysis

2. **Building Selection**
   - Choose between RC and Masonry buildings
   - Currently only RC building analysis is available

3. **Database Creation**
   - Enter building location/area
   - View progress bar during database creation
   - Access the complete database

4. **Parameter Selection**
   - View and select relevant parameters
   - Parameters with >35% significance are highlighted
   - Calculate probability of failure based on selected parameters

5. **Results**
   - View probability calculation
   - Get risk assessment (Low/Moderate/High)
   - Export results to Excel

## Troubleshooting

1. If you encounter "ModuleNotFoundError":
   - Make sure you've activated the virtual environment
   - Reinstall the required packages using pip

2. If Excel files don't open:
   - Ensure you have Microsoft Excel or a compatible spreadsheet application installed
   - Check file permissions in the project directory

3. If the GUI doesn't display properly:
   - Update PySimpleGUI to the latest version:
   ```cmd
   pip install --upgrade PySimpleGUI
   ```

## Notes

- The application requires write permissions in its directory to create and modify Excel files
- Keep all Python files and Excel databases in the same directory
- Don't modify the Excel file structure manually to avoid data corruption

## Support

For any issues or questions, please contact the development team:
- Ishank Singh
- Hemant Singh
- Gautam Tayal

## License

This project is part of an academic research project at [Institution Name]. 