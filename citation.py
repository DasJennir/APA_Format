author_last = input('Enter author\'s last name: ').capitalize()
author_init = input('Enter author\'s initial: ').capitalize()
date = input('Enter publish date, format (e.g: 2018, November 4): ').capitalize()
title_article = input('Enter title of article: ').title()
title_news = input('Title of Online News Paper (e.g: New York Times): ').title()
url = input('Url/Name of the website: ')


if url.startswith('https') or url.startswith('http'):
    pass
else:
    old_url = url
    url = f'https://{old_url}'

class style:
   BOLD = '\033[1m'
   END = '\033[0m'


apa = (f'{author_last}, {author_init}. ({date}). "{title_article}."{ style.BOLD +  title_news + style.END}.Retrieved from {url}')

print(apa)
