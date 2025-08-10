from requests_html import HTMLSession

def weather() :
    s = HTMLSession()
    query = "patan"
    url=f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'})
    temp = r.html.find("span#wob_tm" , first=True).text
    print(temp)
    unit = r.html.find("div.vk_bk wob_unit span.wob_t" , first=True).text
    print(unit)
    desc = r.html.find('span#wob_dc' , first= True).text
    return temp+ " "+unit+ " " +desc