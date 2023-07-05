import re


def checking(comment):
    check_link = re.findall(r'http+', comment)
    print(check_link)
    if len(check_link) > 0:
        return True
    else:
        return False

