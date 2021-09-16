from collections import Counter
def subdomainVisits(cpdomains):
    c = Counter()
    res = []
    for domain in cpdomains:
        freq, url = domain.split(' ')
        
        c[url] += int(freq)
        
        dot = url.find('.')
        while dot != -1:
            c[url[dot + 1:]] += int(freq)
            dot = url.find('.', dot + 1)
    for url in c:
        res.append("{} {}".format(c[url], url))
    return res
history = [
  ["3234.html","xys.html", "7hsaa.html"], # user1
  ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"] # user2
]

def longestCommonHistory(history1, history2):
    if not history1 or not history2:
        return []
    m, n = len(history1), len(history2)

    dp = [[0] * (n +  1) for _ in range(m + 1)]
    res = []
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if history1[i - 1] == history2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > len(res):
                res = history1[i - dp[i][j]:i]
    return res


#print(longestCommonHistory(history[0], history[1]))
completed_purchase_user_ids = [
"3123122444","234111110", "8321125440", "99911063"]

ad_clicks = [
#"IP_Address,Time,Ad_Text",
"122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
"96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
"122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
"82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
"92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
"92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

all_user_ips = [
#"User_ID,IP_Address",
"2339985511,122.121.0.155",
"234111110,122.121.0.1",
"3123122444,92.130.6.145",
"39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
"8321125440,82.1.106.8",
"99911063,92.130.6.144"
]

def conversionRate(completed_purchase_user_ids, ad_clicks, all_user_ips):
    ip2Uid = {}
    for s in all_user_ips:
        uid, ip = s.split(',')
        ip2Uid[ip] = uid
    buyers = set(completed_purchase_user_ids)
    ad_click_counter = {}

    for record in ad_clicks:
        ip, time, ads = record.split(',')
        uid = ip2Uid[ip] if ip in ip2Uid else -1
        bought = 1 if uid in buyers else 0

        if ads not in ad_click_counter:
            ad_click_counter[ads] = [bought, 1]
        else:
            prev = ad_click_counter[ads]
            ad_click_counter[ads] = [prev[0] + bought, prev[1] + 1]
    res = []
    for ads in ad_click_counter.keys():
        bought, clicked = ad_click_counter[ads]
        res.append("{} of {}, {}".format(bought, clicked, ads))
    return res
print(conversionRate(completed_purchase_user_ids, ad_clicks, all_user_ips))
