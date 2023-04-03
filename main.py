import pandas as pd

df = pd.read_csv('''PEN America's Index of School Book Bans (July 1, 2021 - June 30, 2022) - Sorted by Author & Title.csv''')
banned_books = {}
for i, book in df.iterrows():
    author_title = (book['Author'], book['Title'])
    if author_title not in banned_books:
        banned_books[author_title] = set()
    banned_books[author_title].add(book['District'])

banned_books = {k: len(v) for k, v in banned_books.items()}
banned_books = sorted(list(banned_books.items()), key=lambda x: x[1], reverse=True)

import requests
from time import sleep
from selenium import webdriver


sess = requests.Session()
url = 'https://app.thestorygraph.com/browse'



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


query_results = {}
for book in banned_books[:100]:
    author, title = book[0]
    search_query = f'{title} {author}'
    params = {'search_term': search_query}
    r = sess.get(url, params=params, timeout=10)
    print(r, len(r.text))
    query_results[book[0]] = r
    sleep(1)


from bs4 import BeautifulSoup
base_url='https://app.thestorygraph.com'
title_url = {('Kobabe, Maia', 'Gender Queer: A Memoir'): 'https://app.thestorygraph.com/books/6d539db7-d0b7-44bf-9ca9-fbc19047701b', ('Johnson, George M.', "All Boys Aren't Blue"): 'https://app.thestorygraph.com/books/62b8f691-6cb1-4986-9bf1-f046df190f10', ('Pérez, Ashley Hope', 'Out of Darkness'): 'https://app.thestorygraph.com/books/9fe48dd5-654b-4030-99c0-866a740fe609', ('Morrison, Toni', 'The Bluest Eye'): 'https://app.thestorygraph.com/books/10cca41c-5646-4680-93e4-61cb3a8d31b3', ('Evison, Jonathan', 'Lawn Boy'): 'https://app.thestorygraph.com/books/899e0640-412d-428c-aa4b-15a3337ae7e7', ('Thomas, Angie', 'The Hate U Give'): 'https://app.thestorygraph.com/books/f17920fc-2079-4199-bb70-67aed3571715', ('Alexie, Sherman', 'The Absolutely True Diary of a Part-Time Indian'): 'https://app.thestorygraph.com/books/8cf74ccf-09f7-47b1-a1dc-1222c7743b89', ('Andrews, Jesse', 'Me and Earl and the Dying Girl'): 'https://app.thestorygraph.com/books/9575eee5-743b-41bb-848f-8d494bce0c27', ('Hosseini, Khaled', 'The Kite Runner'): 'https://app.thestorygraph.com/books/6c6726eb-8580-4be7-ab60-5ccd073d7ae5', ('Asher, Jay', 'Thirteen Reasons Why'): 'https://app.thestorygraph.com/books/79cb89be-afc9-42d8-9839-772a5260868d', ('Hopkins, Ellen', 'Crank (Crank Series)'): 'https://app.thestorygraph.com/books/248873f0-100d-4efe-8f98-a0c13ae45b61', ('Myracle, Lauren', 'l8r, g8r'): 'https://app.thestorygraph.com/books/06927588-9000-44b6-9917-4f1614ee4056', ('Green, John', 'Looking for Alaska'): 'https://app.thestorygraph.com/books/5be514e8-67a5-4010-8a3a-ddd1506e7e2f', ('Kuklin, Susan', 'Beyond Magenta: Transgender Teens Speak Out'): 'https://app.thestorygraph.com/books/84cffcad-0395-43d0-861c-774b8bf60233', ('Tamaki, Mariko', 'This One Summer'): 'https://app.thestorygraph.com/books/7b66e445-00f7-4f9a-aebe-1c33b3f9048f', ('Telgemeier, Raina', 'Drama: A Graphic Novel'): 'https://app.thestorygraph.com/books/86e3c3af-a267-491f-a934-f240cf613c8d', ('Dawson, Juno', 'This Book Is Gay'): 'https://app.thestorygraph.com/books/129fbfc4-641d-4521-a033-0d90b1afc943', ('Morrison, Toni', 'Beloved'): 'https://app.thestorygraph.com/books/ec568358-1ffd-44db-af36-4c1344b9ec0c', ('Gino, Alex', 'Melissa (George)'): 'https://app.thestorygraph.com/books/b3bb63cd-526c-493b-9cce-1079b3711be5', ('Curato, Mike', 'Flamer'): 'https://app.thestorygraph.com/books/83f6d73e-7abb-443c-8cb7-267bf0411dda', ('Rosen, L. C.', 'Jack of Hearts (and other parts)'): 'https://app.thestorygraph.com/books/e75abdc5-4e9a-4e78-b7d6-85fabff0c0cb', ('Bechdel, Alison', 'Fun Home: A Family Tragicomic'): 'https://app.thestorygraph.com/books/276a1580-85b1-4b7c-be22-3daa2b719e49', ('Picoult, Jodi', 'Nineteen Minutes'): 'https://app.thestorygraph.com/books/fce57caf-37d9-4529-b511-a0dce854037e', ('Atwood, Margaret', "The Handmaid's Tale"): 'https://app.thestorygraph.com/books/623a7568-a386-4f4f-acca-86f32897e064', ('Johnson, Cathy G.', 'The Breakaways'): 'https://app.thestorygraph.com/books/eb3cb51b-847b-4822-9472-dca3a24012e8', ('Reynolds, Jason', 'All American Boys'): 'https://app.thestorygraph.com/books/30cd7e7f-c7c2-48b4-bff7-31ffc4632619', ('Chbosky, Stephen', 'The Perks of Being a Wallflower'): 'https://app.thestorygraph.com/books/36f578d8-ed1f-4a7d-baed-3b570e77ca72', ('Silvera, Adam', 'More Happy Than Not'): 'https://app.thestorygraph.com/books/1103703f-397e-44ed-9586-356a951a1ffb', ('Hopkins, Ellen', 'Tricks (Tricks Series)'): 'https://app.thestorygraph.com/books/43b7ac6d-e125-4f6c-8c6b-1918371c827b', ('McCormick, Patricia', 'Sold'): 'https://app.thestorygraph.com/books/c46f12db-3a6d-44dd-b199-26059a962b8c', ('Slater, Dashka', 'The 57 Bus: A True Story of Two Teenagers and the Crime That Changed Their Lives'): 'https://app.thestorygraph.com/books/3f9f83dc-62c7-459a-a34d-5ec61a129e19', ('Foer, Jonathan Safran', 'Extremely Loud & Incredibly Close'): 'https://app.thestorygraph.com/books/8b64c2d3-0618-44bb-aa14-a57f63e0743a', ('Harris, Robie H.', "It's Perfectly Normal: Changing Bodies, Growing Up, Sex, and Sexual Health"): 'https://app.thestorygraph.com/books/d44273a4-0c96-4153-a539-03024d8d92f9', ('Jackson, Tiffany D.', "Monday's Not Coming"): 'https://app.thestorygraph.com/books/b5376e36-c4b1-477e-ab55-71d8adb446bd', ('Stone, Nic', 'Dear Martin'): 'https://app.thestorygraph.com/books/01f46f24-c506-4ae6-8b7c-b0126b9e9172', ('Maas, Sarah J.', 'A Court of Mist and Fury (A Court of Thorns and Roses Series)'): 'https://app.thestorygraph.com/books/04729ac0-cdb0-45bb-a2cc-a6f9ef413bc2', ('Jennings, Jazz', 'Being Jazz: My Life as a (Transgender) Teen'): 'https://app.thestorygraph.com/books/f5713363-052f-43b1-b71d-93c2d367a31b', ('Katcher, Brian', 'Almost Perfect'): 'https://app.thestorygraph.com/books/780bdeff-3ec8-493e-9415-e87fe716a834', ('Anderson, Laurie Halse', 'Speak'): 'https://app.thestorygraph.com/books/b68c61d1-e975-4ed6-916a-36507b50633a', ('Mathieu, Jennifer', 'The Truth About Alice: A Novel'): 'https://app.thestorygraph.com/books/28dab662-2eb0-4d04-96ea-2585bc38e8d0', ('Duncan, Lois', 'Killing Mr. Griffin'): 'https://app.thestorygraph.com/books/a5499284-6274-4025-aebf-2290f513a828', ('Levithan, David', 'Two Boys Kissing'): 'https://app.thestorygraph.com/books/ed104d6f-91ed-4d01-aaab-6c34f1bf5c46', ('Myracle, Lauren', 'The Infinite Moment of Us'): 'https://app.thestorygraph.com/books/ccf61505-4c33-4310-ad79-bd7633b8f857', ('Reynolds, Jason', 'Stamped: Racism, Antiracism, and You'): 'https://app.thestorygraph.com/books/77d19735-7494-47b3-be10-8ea00de20f5b', ('Rowell, Rainbow', 'Eleanor & Park'): 'https://app.thestorygraph.com/books/f875cde7-755e-4bbb-87ac-d27c6d3495d9', ('Hutchinson, Shaun David', 'We Are the Ants'): 'https://app.thestorygraph.com/books/030f64ec-4014-4bab-8750-afee778864ce', ('Jennings, Jazz', 'I am Jazz'): 'https://app.thestorygraph.com/books/39eb4c0a-72d5-4fc5-bcd7-4b24d14c5b8c', ('Kendi, Ibram X.', 'How to Be an Antiracist'): 'https://app.thestorygraph.com/books/1d582303-eb3a-4481-851c-be4a91b3c7b5', ('Lockhart, E.', "Real Live Boyfriends: Yes. Boyfriends, Plural. If My Life Weren't Complicated, I Wouldn't Be Ruby Oliver"): 'https://app.thestorygraph.com/books/1b92e520-d950-49ac-9c19-f15c7b3c5f0b', ('Richardson, Justin', 'And Tango Makes Three'): 'https://app.thestorygraph.com/books/923e4563-6761-49ff-85db-f53188c1c0bc', ('Sanders, Rob', 'Pride: The Story of Harvey Milk and the Rainbow Flag'): 'https://app.thestorygraph.com/books/2ed77dd1-cc3f-4cef-8aa2-3ce2495562cd', ('Sebold, Alice', 'Lucky'): 'https://app.thestorygraph.com/books/a35c46f8-5db0-4303-b981-01ca7e89ccf8', ('Walls, Jeannette', 'The Glass Castle'): 'https://app.thestorygraph.com/books/626e6837-6f98-4e1c-95e6-742edcca505b', ('Acevedo, Elizabeth', 'The Poet X'): 'https://app.thestorygraph.com/books/77d75d2d-efec-485e-9713-7fc72dc3d0b3', ('Atwood, Margaret', "The Handmaid's Tale: The Graphic Novel"): 'https://app.thestorygraph.com/books/feaa1085-b5cc-45ed-afe3-29ffc6a9b78c', ('Bartoletti, Susan Campbell', 'They Called Themselves The K.K.K.: The Birth of an American Terrorist Group'): 'https://app.thestorygraph.com/books/af3fc404-40f5-4964-aa0d-43404a7d9aea', ('Belge, Kathy', 'Queer: The Ultimate LGBTQ Guide for Teens'): 'https://app.thestorygraph.com/books/99a6d01e-7508-4dcc-81b0-3d7bfc04fd5f', ('Bertie, Alex', 'Trans Mission: My Quest to a Beard'): 'https://app.thestorygraph.com/books/b54764a8-9e60-4331-b97e-6d9f9d69c662', ('Blume, Judy', 'Forever...'): 'https://app.thestorygraph.com/books/d98ae870-55c0-488d-af59-7ff1341c6399', ('Clare, Cassandra', 'City of Heavenly Fire (The Mortal Instruments Series)'): 'https://app.thestorygraph.com/books/57b176ec-674e-4193-9a8a-15b547c0e709', ('Craft, Jerry', 'New Kid'): 'https://app.thestorygraph.com/books/f1fe66ff-663b-48e6-b6f6-6b845f838498', ('Draper, Sharon M.', 'Blended'): 'https://app.thestorygraph.com/books/5b8dfff7-568c-4d4e-8bff-486478312b8b', ('Garvin, Jeff', 'Symptoms of Being Human'): 'https://app.thestorygraph.com/books/b72e765f-5980-494e-9413-52232c4864be', ('Gephart, Donna', 'Lily and Dunkin'): 'https://app.thestorygraph.com/books/9b057506-2f76-40ca-a7c7-8dda6c9fbd86', ('Green, John', 'Will Grayson, Will Grayson (Will Grayson, Will Grayson Series)'): 'https://app.thestorygraph.com/books/dd795fe9-3a57-4641-a7f9-d85e56fa9fbf', ('Gyasi, Yaa', 'Homegoing'): 'https://app.thestorygraph.com/books/31ec3894-5f84-4abf-9cca-f581f1ee5570', ('Hopkins, Ellen', 'Triangles'): 'https://app.thestorygraph.com/books/a4f333eb-6573-40c6-8fb6-d8657c07d9ad', ('Hutchinson, Shaun David', 'Brave Face: A Memoir'): 'https://app.thestorygraph.com/books/4c6c2dd2-5ad0-4e80-9e11-18981c2ccfac', ('Jewell, Tiffany', 'This Book Is Anti-Racist: 20 Lessons on How to Wake Up, Take Action, and Do the Work'): 'https://app.thestorygraph.com/books/d842285b-6ca2-405b-beea-282e2f6acedd', ('Kendi, Ibram X.', 'Stamped from the Beginning: The Definitive History of Racist Ideas in America'): 'https://app.thestorygraph.com/books/f065e0e3-998a-4eca-afd0-eb5070899247', ('Konigsberg, Bill', 'The Music of What Happens'): 'https://app.thestorygraph.com/books/92377a94-94c4-4883-944f-2d7103e14057', ('McCafferty, Megan', 'Sloppy Firsts (Jessica Darling Series)'): 'https://app.thestorygraph.com/books/3fcb074d-8a2e-4f54-8083-c33b9404ba25', ('Polacco, Patricia', "In Our Mothers' House"): 'https://app.thestorygraph.com/books/66fabfa8-37d5-483c-ace7-08c849da7c7d', ('Quintero, Isabel', 'Gabi, a Girl in Pieces'): 'https://app.thestorygraph.com/books/9ed2c306-9e75-49c9-9146-2e1b36b5a082', ('Sáenz, Benjamin Alire', 'Aristotle and Dante Discover the Secrets of the Universe (Aristotle and Dante Series)'): 'https://app.thestorygraph.com/books/623a55f4-7166-42be-820d-dc3ab4d36b23', ('Sánchez, Erika L.', 'I Am Not Your Perfect Mexican Daughter'): 'https://app.thestorygraph.com/books/019764d6-eff8-4f08-9d85-7e3e16328539', ('Scott, Elizabeth', 'Living Dead Girl'): 'https://app.thestorygraph.com/books/59efac36-8580-4717-b664-2c59ef1e05ef', ('Smith, Andrew', 'Grasshopper Jungle (Grasshopper Jungle Series)'): 'https://app.thestorygraph.com/books/454fcc25-91e3-47ea-9020-234a928a9ff5', ('Thomas, Aiden', 'Cemetery Boys'): 'https://app.thestorygraph.com/books/df95682b-d6bf-454c-ac04-2b577b093a0f', ('Albertalli, Becky', 'Simon vs. the Homo Sapiens Agenda (Simonverse Series)'): 'https://app.thestorygraph.com/books/61d4ec93-d2a7-4391-bb47-1d2b8fbffd30', ('Albertalli, Becky', 'The Upside of Unrequited (Simonverse Series)'): 'https://app.thestorygraph.com/books/939999a2-c9e3-4d95-9af6-cc2588dc9ed8', ('Albertalli, Becky', "What If It's Us (What If It's Us Series)"): 'https://app.thestorygraph.com/books/92003b00-72d7-42ce-9b2f-3a021a575057', ('Alexander, Michelle', 'The New Jim Crow: Mass Incarceration in the Age of Colorblindness'): 'https://app.thestorygraph.com/books/98d62b0b-7b34-4b33-a498-faabb63988c2', ('Anderson, Laurie Halse', 'Shout'): 'https://app.thestorygraph.com/books/24ae1125-4a37-4f5b-ba71-c4b9ae677d32', ('Andrews, Jesse', 'The Haters'): 'https://app.thestorygraph.com/books/c719bb45-5a1b-4d1d-9986-7819b3d4a6b5', ('Arnold, Elana K.', 'What Girls Are Made Of'): 'https://app.thestorygraph.com/books/81e1e1ea-ed3d-46cf-a202-b8b8b0f22f2f', ('Atta, Dean', 'The Black Flamingo'): 'https://app.thestorygraph.com/books/6a043538-e656-4325-a8b1-b14d26c1b1a3', ('Bayron, Kalynn', 'Cinderella Is Dead'): 'https://app.thestorygraph.com/books/5589a8db-7d2a-459f-974d-d32c6b39847c', ('Bick, Ilsa J.', "The Sin-Eater's Confession"): 'https://app.thestorygraph.com/books/94ae79ce-eb9f-49a2-8d38-7d65b11013fe', ('Blackall, Sophie', 'The Baby Tree'): 'https://app.thestorygraph.com/books/faeecea6-6234-4f6d-b082-6eb4b82c010d', ('Brown, Echo', 'Black Girl Unlimited: The Remarkable Story of a Teenage Wizard'): 'https://app.thestorygraph.com/books/70d4407d-ec5e-4f1d-8339-386d666897bd', ('Colbert, Brandy', 'Little & Lion'): 'https://app.thestorygraph.com/books/6c069b14-2d44-4e71-9370-095d95b11c17', ('Cook, Trish', 'Notes from the Blender'): 'https://app.thestorygraph.com/books/5ed97461-bbde-4a38-9977-4b05272da79a', ('Coulthurst, Audrey', 'Of Fire and Stars (Of Fire and Stars Series)'): 'https://app.thestorygraph.com/books/aaf1fa9f-01bb-4c63-b9f3-af0b141e2f28', ('Craft, Jerry', 'Class Act'): 'https://app.thestorygraph.com/books/2e8f9311-5779-4412-9489-44c2c0fc552b', ('Glines, Abbi', 'The Vincent Boys (The Vincent Boys Series)'): 'https://app.thestorygraph.com/books/b9629c9b-c21c-44ac-a1cb-c9f00a205f1d', ('Gottfred, B. T.', 'Forever for a Year'): 'https://app.thestorygraph.com/books/6e9dc85b-9eaa-4286-96c5-723f38f7036a', ('Gottfred, B. T.', 'The Nerdy and the Dirty'): 'https://app.thestorygraph.com/books/a282fec0-c57b-4d3b-8977-6cc3c6a22cf8', ('Hartinger, Brent', 'Geography Club (Russel Middlebrook Series)'): 'https://app.thestorygraph.com/books/41603624-40d4-4557-aaa5-0ede9482558c', ('Higginbotham, Anastasia', 'Not My Idea: A Book About Whiteness (Ordinary Terrible Things Series)'): 'https://app.thestorygraph.com/books/9f6d49b3-b13b-4393-90e5-b154cb956998'}


for author_title, r in query_results.items():
    if author_title in title_url:continue
    soup = BeautifulSoup(r.text, 'lxml')
    try:search_results = list(soup.find('span', {"class": "search-results-books-panes"}).children)
    except:search_results=[]
    search_results = [x for x in search_results if x.find('img') != -1]
    for result in search_results:
        title_series_author = list(map(lambda x: x.text, result.find('div', {"class": "book-title-author-and-series"}).find_all('a')))
        if len(title_series_author) == 3:
            title, series, author = title_series_author
        elif len(title_series_author) == 2:
            title, author = title_series_author
        author = ', '.join(author.split(' ')[::-1])
        if (author, title) == author_title:
            title_url[author_title] = base_url + result.find('a')['href']
            break
        else:
            print((author, title), author_title)
    if author_title not in title_url:
        print('find', author_title)
        driver.get(r.url)
        while not driver.current_url.startswith('https://app.thestorygraph.com/books'):
            sleep(1)
        title_url[author_title] = driver.current_url


banned_books = dict(banned_books)
import re
# img, title, series, author,
# num bans, num pages, additional details,
# tags, mood, url
title_details = {}
for author_title, url in list(title_url.items())[:]:
    if author_title in title_details and 'pages' in title_details[author_title]:continue
    title_details[author_title] = {'url': url}
    r = sess.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    image = soup.find(class_="book-cover").img['src']
    title_series_author = re.split('\n+[ \n]*', soup.find('div', {"class": "book-title-author-and-series"}).text.strip())
    title = title_series_author[0]
    series = soup.find('div', {"class": "book-title-author-and-series"}).find('a', {'href': re.compile(r'series')})
    if series:
        series = {'name': series.parent.text, 'url': base_url+series.get('href')}

    authors = soup.find('div', {"class": "book-title-author-and-series"}).find_all('a', {'href': re.compile(r'author')})
    authors = [{'name': x.text, 'url': base_url+x.get('href')} for x in authors]
    num_bans = banned_books[author_title]
    additional_details_elem = soup.find('p', {'class': 'text-sm font-light text-darkestGrey dark:text-grey mt-1'})
    pages_txt = additional_details_elem.find(text=True).strip()
    first_published = additional_details_elem.find('span').find_all('span')[-1].text
    hidden_details = soup.find('div', {'class': "hidden edition-info mt-3"}).text.strip()
    hidden_details = '\n'.join([x for x in hidden_details.split('\n') if not x.startswith('Publisher')] + [first_published])
    tags_and_moods = soup.find('div', {"class": "book-page-tag-section"})
    tags = [x.text for x in tags_and_moods.find_all(class_='text-teal-700')]
    moods = [x.text for x in tags_and_moods.find_all(class_='text-pink-500')]
    title_details[author_title] |= {'image': image, 'title': title, 'series': series, 'authors': authors, 'pages': pages_txt,
                                    'details': hidden_details, 'tags': tags, 'mood': moods, 'url': url, 'bans': num_bans}
    # print(author_title, title_details[author_title])
    sleep(1)


title_torrents = {k:[] for k in title_details.keys()}


for author_title, book in list(title_details.items())[:]:
    if title_torrents[author_title]:
        continue
    print('find', author_title, book['url'])
    driver.get(f'https://www.myanonamouse.net/tor/browse.php?tor%5Btext%5D=%40title%20{book["title"]}%20%40author%20{book["authors"][0]["name"]}')

    sleep(10)
    if len(driver.window_handles) == 1:
        input('done?')
    for tab in driver.window_handles:
        driver.switch_to.window(tab)
        if not driver.current_url.startswith('https://www.myanonamouse.net/t/'):
            continue
        soup = BeautifulSoup(driver.page_source, 'lxml')
        filetypes = soup.find('div', class_="torFileTypes")
        filetypes = ', '.join([x.text for x in filetypes.find_all('a')])
        torrent_details = {'filetypes': filetypes, 'url': driver.current_url}
        title_torrents[author_title].append(torrent_details)
        driver.close()
    for tab in driver.window_handles:
        driver.switch_to.window(tab)


def sort_filetypes(filetypes):
    if "m4b" in filetypes:return 3
    if "mp3" in filetypes:return 2
    if "epub" in filetypes: return 1
    return 0


for k, v in title_details.items():
    details = v['details']
    details = '\n'.join([x for x in details.split('\n') if x != 'missing pub info' and 'Not specified' not in x])
    title_details[k]['details'] = details
    torrents = sorted(title_torrents[k], key=lambda x: sort_filetypes(x['filetypes']))
    title_details[k]['torrents'] = torrents
    title_details[k]['details'] = title_details[k]['details'].split('\n')
    title_details[k]['authors'] = [x for i, x in enumerate(title_details[k]['authors']) if x not in title_details[k]['authors'][i+1:]]



title_details = dict(sorted(list(title_details.items()), key=lambda x: x[1]['bans'], reverse=True))


import pickle
with open('title_details.pkl', 'wb') as f:
    pickle.dump(title_details, f)

with open('title_details.pkl', 'rb') as f:
    title_details = pickle.load(f)
