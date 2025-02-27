cache={}
def get_page(url):
    if cache.get(url):
        return cache(url) #returns cache data
    else:
        data = get_data_from_server(url)
        cache[url]= data #saves the data in your cache list
        return data
    