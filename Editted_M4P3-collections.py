Last editted by: Angeline Hidalgo
Editted on: Februrary 9, 2020
    
# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1863",
    "William Thackeray": "1870",
    "Anthony Trollope": "1889",
    "Gerard Manley Hopkins": "1882"}

# Was originally 'author.items'. Needed to be 'authors.items'
# 'authors' is defined. 'author' is not.
for authors, date in authors.items():
    print("%s" % authors, " died in ", "%s." % date)
