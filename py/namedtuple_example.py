from collections import namedtuple



Product = namedtuple('Product', ('country', 'name', 'brand', 'type', 'price'))


# Country-wise Product Dataset (Full, Unmodified)
products =[

# Global
Product("Global", "Quran", "Islam", "Religious Book", 0),
Product("Global", "Bhagavad Gita", "Hinduism", "Religious Book", 0),
Product("Global", "Vedas", "Hinduism", "Religious Book", 0),
Product("Global", "Guru Granth Sahib", "Sikhism", "Religious Book", 0),
Product("Global", "Bible", "Christianity", "Religious Book", 0),
Product("Global", "Torah", "Judaism", "Religious Book", 0),
Product("Global", "Tripitaka", "Buddhism", "Religious Book", 0),
Product("Global", "Avesta", "Zoroastrianism", "Religious Book", 0),
Product("Global", "Tao Te Ching", "Taoism", "Religious Book", 0),
Product("Global", "Analects", "Confucianism", "Religious Book", 0),

]

for product in products:
    print(product)


Service = namedtuple('Service', ('attr1','attr2','attr3','attr4','attr5','attr6'))

services = ("world","love","peace","health","happiness","forgiveness","knowledge","Connection with Creator")

print(services)
