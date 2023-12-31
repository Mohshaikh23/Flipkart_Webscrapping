# Flipkart Mobiles Web Scraping

This project is a web scraping script that extracts information about mobile phones from Flipkart. It retrieves details such as product name, price, offers, reviews, and additional specifications like RAM, ROM, display, rear camera, and battery. The extracted data is stored in a CSV file.

```bash
from py_scrapo import mobdata
mobdata(upper_range= max_amount_value)
```

## Requirements

- Python 3.x
- pandas
- BeautifulSoup
- requests

## Installation

1.Clone the repository:

```bash
git clone https://github.com/Mohshaikh23/Flipkart_Webscrapping.git
```

2.Install the dependencies

```bash
pip install pandas beautifulsoup4 requests
```

## Usage

1.Open a terminal or command prompt.

2.Navigate to the project directory:

```bash
    cd flipkart-webscraping
```

3.Run the app.py script with a specified input value:

```bash
python app.py
```

4.Enter the desired price range for mobile phones when prompted.

5.The script will scrape the Flipkart website, extract the data, and save it in a CSV file named 'mobiles_under_price.csv'.

## License

This project is licensed under the MIT License.

Feel free to customize and enhance the `README.md` file to include any additional information or instructions specific to your project.
