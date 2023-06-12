import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
import os

def mobdata(upper_range:int):
    
    current_dir = os.getcwd()
    
    test_folder = os.path.join(current_dir, "test")
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)
    
    # URL template for Flipkart
    url_template = "https://www.flipkart.com/search?q=phones+under+{}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}"

    # Empty lists to store data
    Product_Name = []
    description = []
    Price = []
    offer_price = []
    review = []
    tag = []
    rows =[]
    ram, rom, display, rear_camera, battery = [], [], [], [], []

    # Create a dataframe to store the data
    df = pd.DataFrame(columns = ["Product_Name",
                                "description",
                                "Price",
                                "offer_price",
                                "review"])


    # Iterate over each page
    for page in range(0,42):
        
        url = url_template.format(upper_range,page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        
        box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
        
        names = box.select("div._4rR01T")
        for name in names:
            Product_Name = name.text
        
        descr = box.select("ul._1xgFaf")
        for des in descr:
            description = des.text
        
        prices = soup.select("div._3I9_wc._27UcVY")
        for price in prices:
            Price = price.text
        
        offers = box.select("div._30jeq3._1_WHN1")
        for off in offers:
            offer_price = off.text
        
        reviews = box.select("div._3LWZlK")
        for revi in reviews:
            review = revi.text
            
        row = {'Product_Name': Product_Name, 
            'description': description,
            'Price': Price,
            'offer_price': offer_price,
            'review': review}
        
        rows.append(row)
        df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)

    # Extract additional information from the description column
    for i in df["description"]:
        
        # Extract RAM information
        ram_match = re.findall(r'(\d+\s*(GB|MB))\s*RAM', i)
        if ram_match:
            ram.append(ram_match[0][0])
        else:
            ram.append("")

        # Extract ROM information
        rom_match = re.findall(r'(\d+\s*(GB|MB))\s*ROM', i)
        if rom_match:
            rom.append(rom_match[0][0])
        else:
            rom.append("")

        # Extract display information
        display_match = re.findall(r'(\d+(\.\d+)?)\s*cm', i)
        if display_match:
            display.append(float(display_match[0][0]))
        else:
            display.append("")

        # Extract rear camera information
        rear_camera_match = re.findall(r'(\d+(\.\d+)?)\s*MP\s*', i)
        if rear_camera_match:
            rear_camera.append(float(rear_camera_match[0][0]))
        else:
            rear_camera.append("")

        # Extract battery information
        battery_match = re.findall(r'(\d+)\s*mAh\s*Battery', i)
        if battery_match:
            battery.append(float(battery_match[0]))
        else:
            battery.append("")

    # Add additional columns to the dataframe
    df['RAM'] = ram
    df['ROM'] = rom
    df['Display'] = display
    df['Rear_Camera'] = rear_camera
    df['Battery'] = battery
    df = df.drop('description', axis=1)

    #converting dataframe to csv format
    csv_file_path = os.path.join(test_folder, 
                                 "mobiles_under_{}.csv".format(upper_range))
    df.to_csv(csv_file_path)