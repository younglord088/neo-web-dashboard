import requests
import pandas as pd

urls = [
    'https://autowayaustin.com/',
    'https://creditcarsorlando.com/',
    'https://eastonmotors.com/',
    'https://expressauto.com/',
    'https://finesseacar.com/',
    'https://gilbertmotorcompany.com/',
    'https://gobgautos.com/',
    'https://lofimotors.com/',
    'https://midatlanticautofinance.com/',
    'https://neighborhoodautos.com/',
    'https://neo-motors.com/',
    'https://paradisemotors.net/',
    'https://regalcars.com/',
    'https://rockysautocredit.com/',
    'https://saberacceptance.com/',
    'https://solutionsautogroup.com/',
    'https://square1autosales.com/',
    'https://sullivanmotorsnj.com/',
    'https://superiorcarsonline.com/',
    'https://topnotchusedcars.com/',
    'https://vamosauto.us/',
    'https://25wautos.com/',
    'https://865autos.com/'
]

api_key = 'AIzaSyA942H_e2Sx2im9z8wU7vIQU5srqXiJ2Ik'
strategies = ['desktop', 'mobile']
results = []

for url in urls:
    for strategy in strategies:
        api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={api_key}&category=performance&category=accessibility&category=best-practices&category=seo&strategy={strategy}"
        response = requests.get(api_url)
        data = response.json()

        try:
            performance_score = data['lighthouseResult']['categories']['performance']['score'] * 100
            accessibility_score = data['lighthouseResult']['categories']['accessibility']['score'] * 100
            best_practices_score = data['lighthouseResult']['categories']['best-practices']['score'] * 100
            seo_score = data['lighthouseResult']['categories']['seo']['score'] * 100
            pagespeed_link = f"https://developers.google.com/speed/pagespeed/insights/?url={url}&tab={strategy}"

            results.append({
                'url': f"{strategy.capitalize()} - {url}", 
                'performance': performance_score,
                'accessibility': accessibility_score,
                'best_practices': best_practices_score,
                'seo': seo_score,
                'pagespeed_link': pagespeed_link
            })
        except KeyError as e:
            print(f"KeyError for {url} ({strategy}): {e}")
            
            results.append({
                'url': f"{strategy.capitalize()} - {url}",
                'performance': None,
                'accessibility': None,
                'best_practices': None,
                'seo': None,
                'pagespeed_link': pagespeed_link
            })

df = pd.DataFrame(results)

df.to_csv('pagespeed_scores_yash.csv', index=False, columns=['url', 'performance', 'accessibility', 'best_practices', 'seo', 'pagespeed_link'])
print("Data saved to pagespeed_scores_yash.csv")
