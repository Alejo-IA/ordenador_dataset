# Data Sorting Application

This project fetches data from an external API, processes it, and allows users to sort it based on a selected numerical variable using different sorting algorithms.

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/Alejo-IA/ordenador_dataset.git
   cd ordenador_dataset
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Dependencies

The project requires the following Python libraries:
```txt
requests==2.31.0
numpy==1.26.4
pandas==2.1.4
matplotlib==3.8.3
python-dotenv==1.0.1
```

## Usage

Run the main script:
```sh
python main.py
```

The application will retrieve data from the API and provide options to sort it based on user selection.

## API Used

The application fetches cryptocurrency market data from CoinGecko:
```
https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1
```

Ensure you have an active internet connection to fetch the latest data.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

```sh
WARNING API KEY USE BRO. IDK 
```
