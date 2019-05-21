import git
import os
import shutil


class AssetStore:
    def __init__(self, url, cache_base):
        self.repo = git.Repo(url)
        self.cache_base = cache_base

    # return tags in repo
    def tags(self):
        return list(map(str, self.repo.tags))

    # checkout tag in repo
    def checkout(self, tag):
        self.repo.git.checkout(tag)

    # check if cache folder for this tag exists
    def cache_exists(self, tag):
        return os.path.isdir(self.cache_base + '/' + tag)

    # checkout tag and create cache folder for it
    def cache_create(self, tag):
        self.checkout(tag)
        shutil.copytree(self.repo.working_dir + '/assets', self.cache_base + '/' + tag)

    # returns list of assets at <tag>
    def list(self, tag):
        # check if tag is cached already, if not - go for it
        if not self.cache_exists(tag):
            self.cache_create(tag)
        return os.listdir(self.cache_base + '/' + tag)

    # return a tuple (path, fname) - NOT THE FILE - of the <asset> in version <tag>
    def get(self, tag, file):
        # call <list> to ensure that <tag> is cached
        self.list(tag)
        return self.cache_base + '/' + tag, file
