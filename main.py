f = open('CV_PUBLICATIONS.txt')
fo = open('output.txt','w')

for line in f:
    if line.startswith('Book'):
        break
    line_break=line.split('\t')[1]

    # author
    author = line_break.split(', "')[0]
    author = author.replace(',',' and')
    author = '  author    = {' + author + '},\n'

    # title
    title = line_break.split('"')[1]
    title = '  title     = {' + title + '},\n'

    # rest
    rest = line_break.split('"')[2]
    if rest.startswith(','):
        rest = rest.replace(',','',1)
    rest = rest.lstrip()

    # year
    year=''
    rest_sep = rest.split(' ')
    for i in rest_sep:
        if i.startswith('19') or i.startswith('20'):
            year = i[:4]
    # publication
    publi = rest.split(',')[0]
    rest = rest[len(publi) + 2:]

    # start
    start = ''
    pub_name = title.split('{')[1].split(' ')
    try:
        pub_name = pub_name[0] + pub_name[1]
    except:
        pub_name = pub_name[0]
    if 'conference' in publi.lower() or 'workshop' in publi.lower() or 'proceeding' in publi.lower():
        start = '@inproceedings{' + pub_name + year +',\n'
        publi = '  booktitle = {' +publi +'},\n'
    else:
        start = '@article{' + pub_name + year + ',\n'
        publi = '  journal   = {' + publi + '},\n'

    # volume
    volume = ''
    if 'Vol.' in rest:
        volume = '  volume    = {' + rest.split('Vol.')[1].lstrip().split(',')[0] + '},\n'

    # number
    number = ''
    if 'No.' in rest:
        number = '  number    = {' + rest.split('No.')[1].lstrip().split(',')[0] +'},\n'

    # page
    page = ''
    if 'pp.' in rest:
        page = '  pages     = {' + rest.split('pp.')[1].lstrip().split(',')[0] +'},\n'

    year = '  year      = {' + year +'},\n'

    rest += '\n'

    fo.write(start)
    fo.write(author)
    fo.write(title)
    fo.write(publi)
    fo.write(volume)
    fo.write(number)
    fo.write(page)
    fo.write(year)
    fo.write(rest)
    fo.write('}\n')

    print(rest)
