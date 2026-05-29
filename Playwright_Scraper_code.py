from playwright.sync_api import sync_playwright
import time
import csv
import re


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        all_property_urls = []

        for curr_page in range(1, 19):  # change later one
            print(f'Page {curr_page}')

            target_url = f"https://www.zameen.com/Homes/Islamabad_Bani_Gala-340-{curr_page}.html?sort=price_asc"
            page.goto(target_url)

            title = page.title()
            print(f"Page Title: {title}")

            try:
                page.wait_for_selector('a[aria-label="Listing link"]', timeout=1000)

                listing_links = page.locator('a[aria-label="Listing link"]').all()

                for locator in listing_links:
                    href = locator.get_attribute('href')
                    if href:
                        full_url = f"https://www.zameen.com{href}"
                        all_property_urls.append(full_url)
                print(f"Found {len(listing_links)} listings on page {curr_page}.")

            except Exception as e:
                print(f"Error on page {curr_page} (maybe no more listings or bot detection): {e}")
                break

        print(f"Total property URLs collected: {len(all_property_urls)}")

        with open('zameen_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow([
                'property_type', 'price', 'area', 'beds', 'baths',
                'built_year', 'servant_quarters', 'floors', 'parking_spaces', 'furnished'
            ])

            for url in all_property_urls[5:]:
                print(f"Scraping: {url}")
                try:
                    page.goto(url)
                    page.wait_for_selector('ul[aria-label="Property details"]')

                    details_table = page.locator('ul[aria-label="Property details"]')

                    property_type = details_table.locator('span[aria-label="Type"]').inner_text()
                    price = details_table.locator('span[aria-label="Price"]').inner_text()
                    area = details_table.locator('span[aria-label="Area"]').inner_text()

                    try:
                        beds = details_table.locator('span[aria-label="Beds"]').inner_text()
                    except:
                        beds = "N/A"

                    try:
                        baths = details_table.locator('span[aria-label="Baths"]').inner_text()
                    except:
                        baths = "N/A"


                    page_text = page.locator('body').inner_text()

                    year_match = re.search(r'Built in year:\s*(\d+)', page_text)
                    built_year = year_match.group(1) if year_match else "N/A"

                    sq_match = re.search(r'Servant Quarters:\s*(\d+)', page_text)
                    servant_quarters = sq_match.group(1) if sq_match else "0"

                    floors_match = re.search(r'Floors:\s*(\d+)', page_text)
                    floors = floors_match.group(1) if floors_match else "1"

                    parking_match = re.search(r'Parking Spaces:\s*(\d+)', page_text)
                    parking = parking_match.group(1) if parking_match else "0"

                    furnished = "Yes" if re.search(r'\bFurnished\b', page_text) else "No"

                    writer.writerow([
                        property_type, price, area, beds, baths,
                        built_year, servant_quarters, floors, parking, furnished
                    ])

                except Exception as e:
                    print(f"Failed to scrape {url}. Error: {e}")

                time.sleep(2)


if __name__ == "__main__":
    main()