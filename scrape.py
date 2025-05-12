from playwright.sync_api import sync_playwright
import json
import bs4


def scrape():
    page = 10
    reports = []
    try:
        while page < 597:
            print(f"Page: {page}")
            try:
                with sync_playwright() as p:
                    browser = p.chromium.launch(headless=True)
                    website = browser.new_page()
                    website.goto('https://xeno-canto.org/explore?query=cnt%3A%22%3DPeru%22+grp%3A%22birds%22&pg=' + str(page))
                    website.wait_for_timeout(2000)
                    html = website.content()
                    soup = bs4.BeautifulSoup(html, 'html.parser')
                    with open('output.html', 'w') as f:
                        f.write(html)
                    
                    trs = soup.find_all('tr')
                    print(f"Found {len(trs)} rows")
                    for tr in trs:
                        print('Processing row')
                        try:
                            if tr.find('td').find('div') and tr.find_all('td')[1].find_all('span')[1].text != "Identity unknown (bird) " and tr.find_all('td')[1].find_all('span')[1].text != "Soundscape":
                                reports.append({'name': tr.find_all('td')[1].find('span').find('a').text, 
                                                'time': tr.find_all('td')[2].text, 
                                                'audio': 'https:' + tr.find('td').find('div', class_='xc-mini-audio').find('audio')['src'], 
                                                'grade': tr.find('ul').find('li', class_="selected").find('span').text})
                        except Exception as e:
                            print(e)
            except Exception as e:
                print(e)
            page += 1
    except KeyboardInterrupt:
        pass
    print(f"Total reports: {len(reports)}")
    with open('output.txt', 'w') as f:
        f.write(json.dumps(reports, indent=4))

if __name__ == '__main__':
    scrape()