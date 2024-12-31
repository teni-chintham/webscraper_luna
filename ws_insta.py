import requests  # Library for making HTTP requests
from bs4 import BeautifulSoup  # Library for parsing HTML and XML documents
import random  # Library for generating random values
import time  # Library for time-related functions

# List of Instagram account usernames
target_usernames = [
    "printondemandindia", "inkingo__", "melangebox", "nativetrade_", "urbanneedsin", 
    "qikinkhq", "bizarrely.in", "cactusltd", "shop_haavah", "designedbysensation", 
    "clothingphlox", "d.teestreet", "freakyxclothing", "range.design.store", 
    "aikyamechoes", "ethicl.wear", "bornunborn", "pretclo", "_anokhi_collections_", 
    "pooja_fashion30", "thetrendy_clothes", "the_pyjamacompany", "_jahnvi.creation_", 
    "orange_couture", "theknotted_rope21", "svetibyrajivcreation", 
    "embellish_cottonthreads", "deora_ji__", "yobuddystore", "jugni_attire", 
    "nksboutique2023", "swastikaindia", "girjaa_officials", "radheyranikolkata", 
    "classycloset_____", "_reapsofficial__", "pitara_house", "houseofclothes.in", 
    "1way_menswear", "hustlerclubindia.in", "zubonclassic", "tuckin_menswear", 
    "fealzclothing", "kesarfabric", "attidude_in", "urban.tee.co", "santyk__", 
    "f_and_f_india", "freakers.__", "nuzox.in", "d3_mens_wear._", "basicallybasic.in", 
    "elenthelabel", "cannac.in", "overandout.in", "haqitsallyours", 
    "imhere_clothing", "boldandbroke.in", "sinnersstreet", "ogeez.in", 
    "integriticlothing", "desibelleofficial", "hemstersofficial", "twillsofficial", 
    "sporto.world", "jdcindia", "urban_chaos_wear", "adiaarofficial", 
    "absolutorlife", "modzoneapparels", "new_k.k_ravindera_hosiery", "untangle._", 
    "stylizer.in", "downalley.official", "qarotmen", "clozeet.in", "vudu_india", 
    "mysteryoffashion", "kalimanclub.in", "gamedaywears", "greyheron_", 
    "abodeofeclipse", "citrusclothing.in", "__wakeyourdreams__", "bigbunny.in", 
    "thomasscott.in", "onhete_official", "dreamislandclo", "areandour.in", 
    "byndbaggy", "agthexceptional", "highmaintenance.in", "stosi.in", 
    "ctrl.alt.drip", "vaultclothing.in", "driptrip.co.in", "flaws.in", "beneci.in", 
    "bomaachi", "breakkineven", "beyondextremes.in", "lemonaed.in", 
    "charactr.co.in", "almostsane.in", "street.error", "hopepunk.storee", 
    "5feet11", "te.legacy", "beawrr_", "blanc.earth", "subtract.in", "selectedindia", 
    "cottonfolk.in", "neverneud", "mrbutton", "tessato.co", "tauxxic", "91avnue", 
    "labelcocoloco", "antifragility_official", "sila__atelier", "pul.ovr", 
    "9899.in", "tealclothing.in", "risate.clothing", "attiraante_official", 
    "dripmylook", "utopianproject.in", "therhetoric.in", "alien8.in", 
    "lethalstudios.in", "naasiempire", "audeverse", "thirtythreebands", 
    "headhighstreet", "friday_rituals", "earlyfuture.in", "fallacieapparel", 
    "ofthechaos_", "themangastore.in", "thefitcheck.in", "fmagnetclothing", 
    "turnt.up.clothing", "ofdarac", "algos.in", "urbanprospect", "adlt.in", 
    "arlostore.official", "bindas_apparel", "holyheaden.in", "urbanfits.co.in", 
    "beliore.clothing", "untld.in", "pinkmatter.shop", "7shoresclothing", 
    "gabbana.fashion", "offbeatoutfits_official", "bluebrew.in", "wearduds", 
    "mascln_sassafras", "dawntownclothing", "boseys_", "fadlclo", 
    "greyhound.original", "walawalistudio", "glitchclothing.co", "loudless.in", 
    "neolithicfashion"
]

# Proxies for HTTP requests
proxy_list = [
    "http://202.89.106.150:8080", "http://43.204.139.123:8888", "http://103.48.68.36:83",
    "http://13.234.24.116:1080", "http://65.1.40.47:3128", "http://35.154.78.253:3128",
    "http://3.108.115.48:1080", "http://65.1.244.232:80", "http://13.126.79.133:3128",
    "http://103.48.68.110:83", "http://113.212.87.242:83", "http://203.115.101.51:82",
    "http://203.115.101.55:82", "http://103.105.224.181:8083", "http://43.204.139.123:8888",
    "http://14.139.219.232:8080", "http://13.126.184.76:1080"
]

# Function to check functional proxies
def check_proxy(proxy):
    try:
        response = requests.get('http://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Proxy {proxy} is functional.")
            return proxy
    except requests.exceptions.RequestException:
        print(f"Proxy {proxy} is not functional.")
    return None

# Validate and filter functional proxies
functional_proxies = [check_proxy(proxy) for proxy in proxy_list]
functional_proxies = list(filter(None, functional_proxies))

# Function to scrape profile information
def scrape_profile(username):
    # Construct the URL for the Instagram profile
    url = f"https://www.instagram.com/{username}/"
    proxy = random.choice(functional_proxies)  # Randomly select a functional proxy
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        # Make the HTTP GET request using a proxy
        response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy}, timeout=10)
        response.raise_for_status()  # Raise exception if response contains HTTP error
        soup = BeautifulSoup(response.text, "html.parser")  # Parse HTML content

        # Extract account name and followers
        account_name = soup.find("meta", property="og:title")
        followers = soup.find("meta", property="og:description")
        if account_name and followers:
            name = account_name["content"].split("•")[0].strip()
            followers_count = followers["content"].split("-")[0].split()[0].strip()
            print(f"Name: {name}, Followers: {followers_count}, URL: {url}")
        else:
            print(f"Could not extract data for {username}.")

        # Find similar accounts
        similar_accounts = find_similar_accounts(soup)
        return similar_accounts

    except requests.RequestException as e:
        print(f"Error scraping {username}: {e}")
        return []

# Function to find similar accounts
def find_similar_accounts(soup):
    similar_accounts = []
    try:
        # Locate the "Suggested for You" section or related accounts
        suggested_links = soup.find_all("a", href=True)
        for link in suggested_links:
            href = link["href"]
            if href.startswith("/"):
                similar_username = href.strip("/")
                if similar_username not in similar_accounts and similar_username != "":
                    similar_accounts.append(similar_username)
    except Exception as e:
        print(f"Error finding similar accounts: {e}")
    return similar_accounts

# Main loop
all_usernames = set(target_usernames)  # To avoid duplicates
for username in target_usernames:
    print(f"Scraping profile: {username}")
    similar_accounts = scrape_profile(username)  # Scrape profile and find similar accounts
    all_usernames.update(similar_accounts)  # Add new accounts to the set
    time.sleep(random.uniform(5, 10))  # Random delay between requests

# Print all collected usernames
print("\nCollected usernames:")
print(all_usernames)