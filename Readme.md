

---

# Phone Number Location Tracker

This Python script retrieves the country/region and service provider information associated with a phone number. It then uses the OpenCage Geocoding API to determine the latitude and longitude of the country/region and generates a map with a marker at that location using Folium. The map is saved as an HTML file.

## Features

- Retrieves the **country/region** associated with a phone number.
- Identifies the **service provider** (carrier) of the phone number.
- Uses the **OpenCage Geocoding API** to obtain the latitude and longitude of the country/region.
- Displays the location on a map using **Folium** and saves the map as an HTML file.

## Prerequisites

Make sure you have the following Python libraries installed:

```bash
pip install phonenumbers opencage folium
```

You will also need an **OpenCage Geocoding API key**. You can get one by signing up at [OpenCage's website](https://opencagedata.com/).

## Setup

1. Clone the repository or download the script.
2. Modify the `myphoneno.py` file to include the phone number you want to track in the correct format:
   - Example: `+14158586273` (replace this with your phone number , Don't forget to add your Country Code).

3. Replace the API key `"7227db11613042a29c3bb63b4d658acd"` in the script with your own OpenCage Geocoding API key.

## Usage

1. Run the script from your terminal:

   ```bash
   python your_script_name.py
   ```

2. The script will output:
   - The country/region where the phone number is registered.
   - The service provider for the phone number.
   - The latitude and longitude of the location.
   
3. The script generates a map with the location marked, saved as `mylocation.html`. Open this file in a web browser to view the map.

## Example Output

```bash
The phone number is from the country: United States
The service provider for this phone number is: AT&T
Latitude: 37.0902, Longitude: -95.7129
```

## Code Explanation

1. **Phone Number Parsing and Country Lookup**:
   - The script uses `phonenumbers` to parse the input phone number and retrieves the country/region where it is registered.
   
2. **Service Provider Information**:
   - The carrier (service provider) of the phone number is also retrieved using `phonenumbers`.

3. **Geocoding and Map Generation**:
   - The script uses the **OpenCage Geocoding API** to find the latitude and longitude of the region based on the country.
   - The location is then displayed on a map using the **Folium** library, and the map is saved as an HTML file for easy viewing.

## Limitations

- The location information retrieved is based on the **registered country/region**, not the real-time location of the phone.
- **Precise or real-time location tracking** using a phone number is not possible with this script.






---

