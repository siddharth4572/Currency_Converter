# Currency Converter

## Description
A simple currency converter application built with Python using Tkinter for the graphical user interface. The application fetches real-time exchange rates from an external API and allows users to convert amounts between different currencies.

## Features
- User-friendly interface for currency conversion.
- Fetches real-time exchange rates.
- Supports multiple currencies.
- Displays conversion results clearly.

## Installation
1. Ensure you have Python installed on your machine.
2. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
3. Navigate to the project directory:
   ```bash
   cd currency_converter
   ```
4. Install the required packages:
   ```bash
   pip install requests
   ```

## Usage
1. Run the application:
   ```bash
   python currency_converter.py
   ```
2. Enter the amount in Indian Rupees (₹).
3. Select the currencies you want to convert from and to.
4. Click the "Convert" button to see the converted amount.

## API Information
The application uses the ExchangeRate-API to fetch the latest exchange rates. The API endpoint used is:
```
https://api.exchangerate-api.com/v4/latest/INR
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Siddharth Katyal
