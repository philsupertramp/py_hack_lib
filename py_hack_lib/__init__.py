import urllib.request


def get_company_icon(url):
    """
    get_icon(url) returns the link of a favicon/icon of a given website
    :param url: url where the icon should get from
    :return: returns url of the url's favicon/icon
    """
    homepage = urllib.request.urlopen(url)
    homepage = str(homepage.read())
    if homepage.find('icon') > 0:
        page = homepage.split('icon', 1)[1]  # search for icon/favicon part
        page = page.split('href="', 1)[1]  # get href url
        page = page.split('"', 1)[0]  # cut substr after url
        if page.find('https://') < 0 and page.find('http://') < 0:
            page = url+page  # if url points to local directory append given url with directory
        icon = urllib.request.urlopen(page)  # check filetype in icon/favicon url

        if icon.info().get('Content-Type').find('image') >= 0:
            return page
    if homepage.find('property="og:image"') > 0:
        page = homepage.split('property="og:image"', 1)[1]
        page = page.split('content="', 1)[1]
        page = page.split('"', 1)[0]
        if page.find('https://') < 0 and page.find('http://') < 0:
            page = url+page  # if url points to local directory append given url with directory
        icon = urllib.request.urlopen(page)  # check filetype in icon/favicon url
        if icon.info().get('Content-Type').find('image') >= 0:
            return page

    return None


def middle_cut(value, arg):
    """Returns first or second half of string"""
    new = strip_tags(value)
    mid = int(len(str(new).split(' '))/2)
    half = new.split(' ', mid)[mid]
    half = half.split(' ', 1)[0]
    mid_t = value.find(half)
    mid = [value[0:mid_t], value[mid_t:len(value)]]
    return mid[arg-1]

