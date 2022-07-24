import os

res = {}


def read_content(url, prev):
    if url.split('\\')[-1].startswith('1'):
        with open(url, encoding='utf-8') as f:
            content = f.read().rstrip('\n')
            lst = content.split('\n')
            corr_lst = [item.rstrip('\t') for item in lst]
            if prev not in res:
                res[prev] = [corr_lst]
            else:
                res[prev].append(corr_lst)
    else:
        with open(url, encoding='utf-8') as f:
            content = f.read().rstrip('\n')
            lst = content.split('\n')
            for item in lst:
                process = item.split('：')
                # print(process,prev)
                if len(process) > 1 and process[0] not in res:
                    res[process[0]] = []
                # print(f'{process[0]}___{prev}:{process[1]}')
                res[process[0]].append(f'{prev}:{process[1]}')


def scaner_file(url):
    paths = os.listdir(url)
    for path in paths:
        real_url = os.path.join(url, path)
        if os.path.isfile(real_url):
            read_content(real_url, real_url.split('\\')[-2])
        elif os.path.isdir(real_url):
            scaner_file(real_url)


scaner_file('C:\\Users\\dyedd\\Desktop\\1\\')

for i in res:
    content = ''
    h = ''
    for m in res[i]:
        if isinstance(m,list):
            content = '\n'.join(m)
        else:
            h += f'{m}\n'
    print(f'{i}同志发言做自我批评：\n{content}\n其他党员同志对其提出批评意见：\n{h}')